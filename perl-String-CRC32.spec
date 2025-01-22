#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-String-CRC32
Version  : 2.100
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/String-CRC32-2.100.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/String-CRC32-2.100.tar.gz
Source1  : http://ftp.debian.org/debian/pool/main/libs/libstring-crc32-perl/libstring-crc32-perl_2-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-String-CRC32-license = %{version}-%{release}
Requires: perl-String-CRC32-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
String::CRC32 - Perl interface for cyclic redundancy check generation
# SYNOPSIS

%package dev
Summary: dev components for the perl-String-CRC32 package.
Group: Development
Provides: perl-String-CRC32-devel = %{version}-%{release}
Requires: perl-String-CRC32 = %{version}-%{release}

%description dev
dev components for the perl-String-CRC32 package.


%package license
Summary: license components for the perl-String-CRC32 package.
Group: Default

%description license
license components for the perl-String-CRC32 package.


%package perl
Summary: perl components for the perl-String-CRC32 package.
Group: Default
Requires: perl-String-CRC32 = %{version}-%{release}

%description perl
perl components for the perl-String-CRC32 package.


%prep
%setup -q -n String-CRC32-2.100
cd %{_builddir}
tar xf %{_sourcedir}/libstring-crc32-perl_2-1.debian.tar.xz
cd %{_builddir}/String-CRC32-2.100
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/String-CRC32-2.100/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-CRC32
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-String-CRC32/e644c70f7588a15bb62c2add251c60e1125351ce || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::CRC32.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-CRC32/e644c70f7588a15bb62c2add251c60e1125351ce

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
