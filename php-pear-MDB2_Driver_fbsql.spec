%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_fbsql
%define		_status		alpha
%define		_pearname	MDB2_Driver_fbsql

Summary:	%{_pearname} - fbsql MDB2 driver
Summary(pl):	%{_pearname} - sterownik fbsql dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ea6439e7740b79060e14e16b178b5333
URL:		http://pear.php.net/package/MDB2_Driver_fbsql/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.3.0
Requires:	php-pear-PEAR >= 1:1.0b1
Requires:	php-pear-MDB2 >= 2.0.0beta6
Requires:	php-fbsql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Frontbase SQL MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
Sterownik Fronbase SQL dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/fbsql.php
%{php_pear_dir}/MDB2/Driver/Manager/fbsql.php
%{php_pear_dir}/MDB2/Driver/Native/fbsql.php
%{php_pear_dir}/MDB2/Driver/Reverse/fbsql.php
%{php_pear_dir}/MDB2/Driver/fbsql.php
%{php_pear_dir}/package_fbsql.php
