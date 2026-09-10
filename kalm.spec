%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Name:		kalm
Version:	26.08.1
Release:	1
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Breathing techniques trainer
URL:		https://apps.kde.org/kalm/
License:	LGPLv2+
Group:		Graphical desktop/KDE
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6QQC2DesktopStyle)

%description
Kalm teaches different breathing techniques.

%files -f %{name}.lang
%{_bindir}/kalm
%{_datadir}/applications/org.kde.kalm.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kalm.svg
%{_datadir}/metainfo/org.kde.kalm.appdata.xml
