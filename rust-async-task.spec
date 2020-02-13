# Generated by rust2rpm 13
# testing needs an alpha pin-utils
%bcond_with check
%global debug_package %{nil}

%global crate async-task

Name:           rust-%{crate}
Version:        1.3.1
Release:        1%{?dist}
Summary:        Task abstraction for building executors

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/async-task
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         async-task-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Task abstraction for building executors.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Wed Dec 25 09:25:18 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Fri Dec 20 16:20:09 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
