Name:    qtlottie
Summary: Qt Lottie-Animations
Version: 5.15.1
Release: 1
License: GPLv3
URL:     https://code.qt.io/cgit/qt/qtlottie.git
Source0: %{name}-%{version}.tar.bz2
Patch0:  0001-Define-qAsConst.patch

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)

%package devel
Summary:  %{summary} - development files
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(Qt5Core)
Requires: pkgconfig(Qt5Gui)
Requires: pkgconfig(Qt5Quick)

%package plugin
Summary:  %{summary} plugin
Requires: %{name} = %{version}-%{release}

%description
Lottie is a family of player software for a certain json-based file format for describing 2d vector graphics animations. These files are created/exported directly from After Effects by a plugin called Bodymovin.

%description devel
This package contains development files for %{summary}

%description plugin
This package contains %{summary} plugin

%prep
%setup -q -n %{name}-%{version}/upstream
%patch0 -p1

%build
touch .git # magic!
%qmake5 \
    QT_BUILD_PARTS+=tests \
    QMF_INSTALL_ROOT=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libQt5Bodymovin.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtBodymovin
%{_libdir}/libQt5Bodymovin.so
%{_libdir}/libQt5Bodymovin.la
%{_libdir}/libQt5Bodymovin.prl
%{_datadir}/qt5/mkspecs/modules/qt_lib_bodymovin_private.pri

%files plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/Qt/labs/lottieqt/lib*.so
%{_libdir}/qt5/qml/Qt/labs/lottieqt/plugins.qmltypes
%{_libdir}/qt5/qml/Qt/labs/lottieqt/qmldir
