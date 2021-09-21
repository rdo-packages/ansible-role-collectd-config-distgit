%global srcname collectd_config_ansible_role

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%{?dlrn: %global tarsources ansible-role-collectd-config}
%{!?dlrn: %global tarsources collectd-config-ansible-role}

Name:           ansible-role-collectd-config
Version:        0.0.1
Release:        1%{?dist}
Summary:        Ansible role for creating collectd configs

License:        ASL 2.0
URL:            https://github.com/infrawatch/collectd-config-ansible-role
Source0:        https://github.com/infrawatch/collectd-config-ansible-role/archive/%{upstream_version}/collectd-config-ansible-role-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core

Requires:       (python3dist(ansible) or ansible-core)

%description

Ansible role for creating collectd configs

%prep
%autosetup -n %{tarsources}-%{upstream_version} -S git


%build


%install
mkdir -p  %{buildroot}%{_datadir}/ansible/roles/collectd_config
cp -r ./* %{buildroot}%{_datadir}/ansible/roles/collectd_config


%files
%doc README*
%license LICENSE
%{_datadir}/ansible/roles/collectd_config
%exclude %{_datadir}/ansible/role/collectd_config/tests/*

%changelog
* Tue Aug 17 2021 RDO <dev@lists.rdoproject.org> 0.0.1-1
- Update to 0.0.1


