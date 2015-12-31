Name:           ros-indigo-husky-base
Version:        0.2.5
Release:        0%{?dist}
Summary:        ROS husky_base package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/husky_base
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-diff-drive-controller
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-husky-control
Requires:       ros-indigo-husky-description
Requires:       ros-indigo-husky-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-husky-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-sensor-msgs

%description
Clearpath Husky robot driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 31 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.5-0
- Autogenerated by Bloom

* Wed Jul 08 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.4-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.3-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.2-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.1-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.0-0
- Autogenerated by Bloom

