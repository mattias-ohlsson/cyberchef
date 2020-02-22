Name:           cyberchef
Version:        9.13.1
Release:        1%{?dist}
Summary:        The Cyber Swiss Army Knife

License:        ASL 2.0
URL:            https://github.com/gchq/CyberChef
Source0:        https://github.com/gchq/CyberChef/releases/download/v%{version}/CyberChef_v%{version}.zip
Source1:        https://raw.githubusercontent.com/gchq/CyberChef/master/LICENSE
Source2:        https://raw.githubusercontent.com/gchq/CyberChef/master/README.md
Source3:        https://raw.githubusercontent.com/gchq/CyberChef/master/CHANGELOG.md
Source4:        %{name}.desktop
BuildArch:      noarch

BuildRequires:  desktop-file-utils
Requires:       firefox

%description
A simple, intuitive web app for analysing and decoding data without having to
deal with complex tools or programming languages. CyberChef encourages both
technical and non-technical people to explore data formats, encryption and
compression.

%prep
%autosetup -c

# Add CHANGELOG.md, LICENSE and README.md
cp -a %{SOURCE1} LICENSE
cp -a %{SOURCE2} README.md
cp -a %{SOURCE3} CHANGELOG.md

%build
mv CyberChef_v%{version}.html cyberchef.html

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 cyberchef.html %{buildroot}%{_datadir}/%{name}
cp -r assets/ %{buildroot}%{_datadir}/%{name}/
cp -r images/ %{buildroot}%{_datadir}/%{name}/
install -m 644 -D images/cyberchef-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE4}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/assets/main.css
%{_datadir}/%{name}/assets/main.js
%{_datadir}/%{name}/assets/fonts/*.fnt
%{_datadir}/%{name}/assets/fonts/*.png
%{_datadir}/%{name}/assets/tesseract/lang-data/eng.traineddata.gz
%{_datadir}/%{name}/assets/tesseract/*.js
%{_datadir}/%{name}/images/*.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Feb 22 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 9.13.1-1
- Initial build
