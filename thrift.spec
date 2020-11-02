Name:           thrift
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Software framework for cross-language services development
Group:          System Environment/Libraries
License:	Apache 2.0
URL:            https://github.com/jaegertracing/jaeger-client-cpp
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: boost-static
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libevent-devel
BuildRequires: libstdc++-devel
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: texlive
BuildRequires: zlib-devel

%description
	
The Apache Thrift software framework for cross-language services
development combines a software stack with a code generation engine to
build services that work efficiently and seamlessly between C++, Java,
Python, %{?php_langname}and other languages.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup

%build
sh ./bootstrap.sh
%configure --disable-dependency-tracking --disable-static --with-boost=/usr 
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}/usr/lib64/python2.7

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig
	
%files
%doc LICENSE NOTICE
%{_bindir}/thrift
%{_libdir}/libthrift-%{version}.so
%{_libdir}/libthriftz-%{version}.so
%{_libdir}/libthriftnb-%{version}.so

%files devel
%{_includedir}/thrift
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.0
%{_libdir}/pkgconfig/*.pc
%doc LICENSE NOTICE

%changelog
