Summary:	PCW Explorer - reading PCW disks, converting images into PNG or JPG
Summary(pl):	PCW Explorer - odczyt dyskietek PCW, konwersja obrazków do PNG lub JPG
Name:		pcwplore
Version:	0.02
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://www.seasip.demon.co.uk/Unix/PcwPlore/%{name}_src.zip
# Source0-md5:	886c04a3331955efe91dfcddf40391ea
URL:		http://www.seasip.demon.co.uk/Unix/PcwPlore/
BuildRequires:	unzip
BuildRequires:	wxGTK2-devel >= 2.4
Requires:	cpmtools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCW Explorer is capable of reading PCW discs, and of converting image
files into PNG or JPG format.

%description -l pl
PCW Explorer potrafi czytaæ dyskietki PCW i konwertowaæ pliki obrazków
do formatu PNG lub JPG.

%prep
%setup -q -c

%build
%{__make} -C imtypes \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} `wxgtk2-2.4-config --cflags`"

%{__make} \
	DISKDEFS="%{_datadir}/misc/diskdefs" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="\$(CPMTOOLS_FLAGS) %{rpmcflags} -Wall -Iimtypes" \
	CXXFLAGS="\$(CPMTOOLS_FLAGS) %{rpmcflags} -Wall -Iimtypes `wxgtk2-2.4-config --cflags`" \
	LFLAGS="%{rpmldflags} `wxgtk2-2.4-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pcwplore $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
