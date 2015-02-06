%define upstream_name    MooseX-Declare
%define upstream_version 0.35

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Handle method modifier declarations
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::Declare)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Method::Signatures)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This module provides syntactic sugar for Moose, the postmodern object
system for Perl 5. When used, it sets up the 'class' and 'role' keywords.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.340.0-2mdv2011.0
+ Revision: 653602
- rebuild for updated spec-helper

* Sat Sep 04 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 575746
- update to 0.34

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2011.0
+ Revision: 554234
- import perl-MooseX-Declare


* Fri Jul 16 2010 cpan2dist 0.33-1mdv
- initial mdv release, generated with cpan2dist
