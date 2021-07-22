#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : freezegun
Version  : 1.1.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/1f/3a/92d1dbf22d7227548a15900bbeff64ed8f43e9b1aeba3a5850ff4e439508/freezegun-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/3a/92d1dbf22d7227548a15900bbeff64ed8f43e9b1aeba3a5850ff4e439508/freezegun-1.1.0.tar.gz
Summary  : Let your Python tests travel through time
Group    : Development/Tools
License  : Apache-2.0
Requires: freezegun-license = %{version}-%{release}
Requires: freezegun-python = %{version}-%{release}
Requires: freezegun-python3 = %{version}-%{release}
Requires: python-dateutil
BuildRequires : buildreq-distutils3
BuildRequires : python-dateutil

%description
====================================================

%package license
Summary: license components for the freezegun package.
Group: Default

%description license
license components for the freezegun package.


%package python
Summary: python components for the freezegun package.
Group: Default
Requires: freezegun-python3 = %{version}-%{release}

%description python
python components for the freezegun package.


%package python3
Summary: python3 components for the freezegun package.
Group: Default
Requires: python3-core
Provides: pypi(freezegun)
Requires: pypi(python_dateutil)

%description python3
python3 components for the freezegun package.


%prep
%setup -q -n freezegun-1.1.0
cd %{_builddir}/freezegun-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611155102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freezegun
cp %{_builddir}/freezegun-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/freezegun/83ff4be984d95e17546d5eaa6e14beba8ef4b5e9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/freezegun/83ff4be984d95e17546d5eaa6e14beba8ef4b5e9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
