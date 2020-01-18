Name:           perl-Sub-Install
Version:        0.926
Release:        6%{?dist}
Summary:        Install subroutines into packages easily
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sub-Install/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Sub-Install-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%if !%{defined perl_bootstrap}
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
%endif

%description
This module makes it easy to install subroutines into packages without the
unslightly mess of no strict or typeglobs lying about where just anyone
can see them.

%prep
%setup -q -n Sub-Install-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
# you'll note a number of tests are skipped due to Test::Output not being
# present.  However, Test::Output requires Sub::Exporter which requires...
# Sub::Install.  Holy circular loop, Batman!  :)
%if !%{defined perl_bootstrap}
PERL_TEST_CRITIC=1 make test
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.926-6
- Mass rebuild 2013-12-27

* Mon Aug 20 2012 Petr Pisar <ppisar@redhat.com> - 0.926-5
- Specify all dependencies

* Wed Aug 15 2012 Daniel Mach <dmach@redhat.com> - 0.926-4.1
- Rebuild for perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.926-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.926-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.926-2
- Perl 5.16 rebuild

* Mon Mar 12 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.926-1
- Update to 0.926

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.925-9
- Perl mass rebuild
- add perl_bootstrap macro
- add missing BR ExtUtils::MakeMaker

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.925-7
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.925-6
- Mass rebuild with perl-5.12.0

* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.925-5
- add license

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.925-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.925-1
- update to 0.925

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.924-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.924-2
- rebuild for new perl
- fix license tag

* Wed Nov 22 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.924-1
- update to 0.924
- add perl(Test::Perl::Critic) to BR's

* Wed Sep 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.922-2
- bump

* Sat Sep 02 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.922-1
- Specfile autogenerated by cpanspec 1.69.1.
