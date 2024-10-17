%define name totem-plugin-arte
%define version 0.9.2
%define release %mkrel 2

Summary: Arte Totem plugin
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://wenner.ch/files/public/mirror/%name/%name-%version.tar.gz
License: GPLv2+ with exception
Group: Video
Url: https://gitorious.org/totem-plugin-arte
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: vala >= 0.7.10
BuildRequires: libsoup-devel
BuildRequires: libGConf2-devel
BuildRequires: totem-plparser-devel
BuildRequires: gtk2-devel
Requires: totem
Requires: gstreamer0.10-rtmp


%description
This Totem plugin allows you to watch video streams from the
Franco-German TV Channel Arte. http://plus7.arte.tv/ Sadly, this
service is only available for IPs within France, Germany, Belgium or
Switzerland.

%prep
%setup -q
%autopatch -p1


%build
make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang totem-arte

%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif

%clean
rm -rf %{buildroot}

%files -f totem-arte.lang
%defattr(-,root,root)
%doc README NEWS
%_libdir/totem/plugins/arteplus7
%_datadir/totem/plugins/arteplus7
