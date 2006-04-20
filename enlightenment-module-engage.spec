%define		_module_name	engage
%define		_snap	20060419
Summary:	Enlightenment DR17 module: engage
Summary(pl):	Modu³ Enlightenmenta DR17: engage
Name:		enlightenment-module-%{_module_name}
Version:	0.0.9
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/misc/%{_module_name}-%{_snap}.tar.bz2
# Source0-md5:	9e5d1070c9469ca15b0929e6fdb154da
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	ewl-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenmentDR17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Engage is a dockbar based on the Enlightenment Foundation Libraries.
It currently works as an app-launcher, taskbar and a system tray.

%prep
%setup -q -n %{_module_name}
sed 's/ 16\.999/ 0.16.999/' -i configure.in
sed 's@$(libdir)/engage/module@$(e_modules)/engage@' -i src/module/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules_extra/%{_module_name}/module_icon.png
%{_datadir}/%{_module_name}
