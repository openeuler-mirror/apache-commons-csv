Name:                apache-commons-csv
Version:             1.5
Release:             2
Summary:             Utilities to assist with handling of CSV files
License:             ASL 2.0
URL:                 https://commons.apache.org/proper/commons-csv/
BuildArch:           noarch
Source0:             http://archive.apache.org/dist/commons/csv/source/commons-csv-%{version}-src.tar.gz
BuildRequires:       maven-local mvn(commons-io:commons-io) mvn(junit:junit)
BuildRequires:       mvn(org.apache.commons:commons-lang3)
BuildRequires:       mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:       mvn(org.apache.maven.plugins:maven-antrun-plugin)

%description
Commons CSV was started to unify a common and simple interface for
reading and writing CSV files under an ASL license.

%package javadoc
Summary:             API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-csv-%{version}-src
sed -i 's/\r//' *.txt
find -name profile.jacoco -delete
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_dep :h2
rm src/test/java/org/apache/commons/csv/CSVPrinterTest.java
%mvn_file ":{*}" %{name} @1
%mvn_alias : commons-csv:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 14 2020 baizhonggui <baizhonggui@huawei.com> - 1.5-2
- Modify source0

* Sat Jul 25 2020 chengzihan <chengzihan2@huawei.com> - 1.5-1
- Package init
