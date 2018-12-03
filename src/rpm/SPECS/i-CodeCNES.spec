# rpmbuild -bb SPECS/jenkins.spec --define '_topdir '`pwd` -v --clean
%define i_code_cnes_verson 3.1.0
Name:       i-CodeCNES
Version:    %{versionModule}
Release:    %{i_code_cnes_verson}.%{releaseModule}
Epoch:      2
Summary:    Static code analysis tool for Fortan and Shell
Group:      develenv
License:    Eclipse Public License - v 1.0
Packager:   softwaresano.com
URL:        https://github.com/lequal/i-CodeCNES/
BuildArch:  x86_64
BuildRoot:  %{_topdir}/BUILDROOT
Requires:   ss-develenv-user >= 33
Vendor:     softwaresano

%define package_name i-CodeCNES
%define package_home /opt/ss/develenv/dp/platform/%{package_name}

%description
i-Code CNES is a static code analysis tool to help developers write code 
compliant with CNES coding rules for Fortran 77, Fortran 90 and Shell.

# ------------------------------------------------------------------------------
# CLEAN
# ------------------------------------------------------------------------------
%clean
rm -rf $RPM_BUILD_ROOT

# ------------------------------------------------------------------------------
# INSTALL
# ------------------------------------------------------------------------------
%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{package_home}
cd $RPM_BUILD_ROOT/%{package_home}
cd ..
curl -L -k -O https://github.com/lequal/i-CodeCNES/releases/download/v%{i_code_cnes_verson}/i-CodeCNES-%{i_code_cnes_verson}-CLI-linux.gtk.x86_64.zip
unzip i-CodeCNES-%{i_code_cnes_verson}-CLI-linux.gtk.x86_64.zip
chmod 755 icode/icode
rm -rf %{package_name}
mv icode %{package_name}
rm -f i-CodeCNES-%{i_code_cnes_verson}-CLI-linux.gtk.x86_64.zip
# ------------------------------------------------------------------------------
# PRE-INSTALL
# ------------------------------------------------------------------------------
%pre
# ------------------------------------------------------------------------------
# POST-INSTALL
# ------------------------------------------------------------------------------
%post

# ------------------------------------------------------------------------------
# PRE-UNINSTALL
# ------------------------------------------------------------------------------
%preun
# ------------------------------------------------------------------------------
# POST-UNINSTALL
# ------------------------------------------------------------------------------
%postun

%files
%defattr(-,develenv,develenv,-)
%{package_home}/*

