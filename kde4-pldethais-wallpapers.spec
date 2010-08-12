
Summary:	PLDEthais KDE4 wallpapers
Summary(pl.UTF-8):	Tapety do PLDEthais do KDE4
Name:		kde4-pldethais-wallpapers
Version:	0
Release:	1
License:	LGPLv3
Group:		X11/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	a302f918cd427a8a20881ede1cd84742
URL:		http://livecd.pld-linux.org
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLDEthais KDE4 wallpapers.

%description -l pl.UTF-8
Tapety PLDEthais do KDE4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
cp -ar pldethais $RPM_BUILD_ROOT%{_datadir}/wallpapers/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/pldethais
