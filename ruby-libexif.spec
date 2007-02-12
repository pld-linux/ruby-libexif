Summary:	EXIF module for Ruby
Summary(pl.UTF-8):	Moduł EXIF dla Ruby
Name:		ruby-libexif
Version:	0.1.2
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://tam.0xfa.com/ruby-libexif/pkg/%{name}-%{version}.tar.gz
# Source0-md5:	39374f7b99a55da6618bfa3c8e163f5c
URL:		http://tam.0xfa.com/ruby-libexif/
BuildRequires:	libexif-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EXIF module for Ruby.

%description -l pl.UTF-8
Moduł EXIF dla Ruby.

%prep
%setup -q

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitearchdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{ruby_archdir}/exif.so
#%{ruby_rubylibdir}/exif.rb
%{_examplesdir}/%{name}-%{version}
