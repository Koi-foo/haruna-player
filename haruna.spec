Name: haruna
Version: 0.6.3.1
Release: alt1

License: GPL-3.0-or-later
Group: Video
Url: https://invent.kde.org/multimedia/haruna
Packager: Evgeny Chuck <koi at altlinux.org>

Source: %name-%version.tar
# Source-url: https://invent.kde.org/multimedia/haruna/-/archive/v%version/haruna-v%version.tar.gz
BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Fri Jul 16 2021 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml librabbitmq-c libsasl2-3 libstdc++-devel libx265-160 libxcbutil-keysyms pkg-config python-base python-modules python3 qt5-base-devel qt5-declarative-devel samba-common-libs samba-libs sh4

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-quickcontrols2-devel

BuildRequires: libqt5-qml
BuildRequires: libqt5-quick

BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kfilemetadata-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kirigami-devel

BuildRequires: libmpv-devel

Requires: libmpv1
Requires: youtube-dl
Requires: kde5-kio-extras
Requires: plasma5-breeze
Requires: icon-theme-breeze
Requires: kf5-qqc2-desktop-style
Requires: kf5-kirigami
Requires: qt5-graphicaleffects

Summary: Haruna is an open source video player built with Qt/QML and libmpv
Summary(ru_RU.UTF-8): Haruna - это видеоплеер с открытым исходным кодом, созданный с использованием Qt/QML и libmpv

%description
GUI to mpv player for DE KDE5.
Play online videos, through youtube-dl.
Supports youtube playlists.
Auto skip chapter containing certain words.
Configurable shortcuts and mouse buttons.

%description -l ru_RU.UTF-8
Графический интерфейс к mpv-плееру для DE KDE5.
Воспроизведение онлайн-видео через youtube-dl.
Поддерживает плейлисты YouTube.
Автоматический пропуск главы, содержащей определенные слова.
Настраиваемые сочетания клавиш и кнопки мыши.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_bindir/haruna
%_desktopdir/org.kde.haruna.desktop
%_iconsdir/hicolor/256x256/apps/org.kde.haruna.svg
%_datadir/metainfo/org.kde.haruna.metainfo.xml

%changelog
* Fri Jul 16 2021 Evgeny Chuck <koi@altlinux.org> 0.6.3.1-alt1
- initial build for ALT Sisyphus
