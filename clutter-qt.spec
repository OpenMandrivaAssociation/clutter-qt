Name: clutter-qt
Summary: Open GL based interactive canvas library for Qt
Version: 0.9_20090720
Release: %mkrel 1
Group: System/Libraries
License: LGPLv2+
URL: https://www.clutter-project.org/
Source0: http://www.clutter-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
Patch0: clutter-1.0-dependency.patch
Patch1: clutter-qt-0.9_20090720-glib-signals.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: clutter-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libqt4-devel

%description
Clutter is an Open GL based interactive canvas library, designed for creating
fast, mainly 2D single window applications such as media box UIs,
presentations, kiosk style applications and so on.

Clutter Qt is an integration library for using Clutter within Qt. It has a
QWidget subclass that contains a Clutter stage.

%package devel
Summary: Clutter Qt header files and development libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Clutter Qt is an integration library for using Clutter within Qt. It has a
QWidget subclass that contains a Clutter stage.

This package contains the headers files needed to build Qt applications using
Clutter Qt library.

%prep
%setup -q -n %{name}-%{version}
# clutter-1.0-dependency.patch
%patch0 -p1
# clutter-qt-0.9_20090720-glib-signals.patch
%patch1 -p1

%build
autoreconf --install
%configure2_5x \
  --disable-static \
  --with-moc=/usr/lib/qt4/bin/moc

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/libclutter-qt-0.9.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libclutter-qt*so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/clutter-qt*.pc
%{_libdir}/libclutter-qt-*.so

