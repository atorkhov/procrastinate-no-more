%global applet_name procrastinate-no-more
%global git_date 20120110
%global git_commit 809c553

Name:           kde-plasma-procrastinate-no-more
Version:        0.2
Release:        1.%{git_date}git%{git_commit}%{?dist}.R
Summary:        Simple widget for the KDE Plasma Workspaces to help you avoid procrastination

Group:          Applications/Productivity
License:        GPLv2+
URL:            http://kde-apps.org/content/show.php?content=142783
#Source0:        http://kde-apps.org/CONTENT/content-files/142783-procrastinate-no-more-0.2.tar.bz2
Source0:        procrastinate-no-more-0.2.tar.bz2

BuildRequires:  cmake qt-devel kdelibs-devel libkactivities-devel
# For /usr/share/kde4/apps/desktoptheme/:
Requires:       kdebase-runtime

%description
Procrastinate No More is a simple widget for the KDE Plasma Workspaces
to help you avoid procrastination.


%prep
%setup -q -n %{applet_name}


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc CHANGELOG COPYING README THANKS
%{_libdir}/kde4/plasma_applet_%{applet_name}.so
%{_datadir}/kde4/services/plasma-applet-%{applet_name}.desktop
%{_datadir}/kde4/apps/desktoptheme/default/widgets/*
%{_datadir}/icons/hicolor/*/apps/*.png


%changelog
* Sat Jan 14 2012 Alexey Torkhov <atorkhov@gmail.com> - 0.2-1.20120110git809c553.R
- Update release tag

* Thu Jan 05 2012 Alexey Torkhov <atorkhov@gmail.com> - 0.2-1
- Initial package.

