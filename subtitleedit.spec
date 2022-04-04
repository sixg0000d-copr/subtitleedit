Name:           subtitleedit
Version:        3.6.5
Release:        1%{?dist}
Summary:        A subtitle editor

License:        GPLv3
URL:            https://www.nikse.dk/subtitleedit/
Source0:        https://github.com/SubtitleEdit/subtitleedit/releases/download/%{version}/SE%(echo %{version} | tr -d .).zip
Source1:        https://github.com/SubtitleEdit/subtitleedit/raw/%{version}/src/ui/Icons/SE.ico
Source2:        subtitleedit
Source3:        subtitleedit.desktop

BuildRequires:  ImageMagick
BuildRequires:  unzip
Requires:       /usr/bin/mono
Recommends:     (vlc or mpv)
Recommends:     tesseract


%description
Subtitle Edit is a free (open source) editor for video subtitles


%prep


%build
unzip %{S:0} -d      %{_builddir}/subtitleedit
touch                %{_builddir}/subtitleedit/.PACKAGE-MANAGER
convert %{S:1}"[9]"  %{_builddir}/subtitleedit.png


%install
install -m 0755 -vd                                                          %{buildroot}%{_datadir}
install -m 0755 -vd                                                          %{buildroot}%{_datadir}/subtitleedit
install -m 0644 -vp %{_builddir}/subtitleedit/Changelog.txt                  %{buildroot}%{_datadir}/subtitleedit/Changelog.txt
install -m 0644 -vp %{_builddir}/subtitleedit/Interop.QuartzTypeLib.dll      %{buildroot}%{_datadir}/subtitleedit/Interop.QuartzTypeLib.dll
install -m 0644 -vp %{_builddir}/subtitleedit/libse.dll                      %{buildroot}%{_datadir}/subtitleedit/libse.dll
install -m 0644 -vp %{_builddir}/subtitleedit/LICENSE.txt                    %{buildroot}%{_datadir}/subtitleedit/LICENSE.txt
install -m 0644 -vp %{_builddir}/subtitleedit/Newtonsoft.Json.dll            %{buildroot}%{_datadir}/subtitleedit/Newtonsoft.Json.dll
install -m 0644 -vp %{_builddir}/subtitleedit/NHunspell.dll                  %{buildroot}%{_datadir}/subtitleedit/NHunspell.dll
install -m 0644 -vp %{_builddir}/subtitleedit/preview.mkv                    %{buildroot}%{_datadir}/subtitleedit/preview.mkv
install -m 0644 -vp %{_builddir}/subtitleedit/SubtitleEdit.exe               %{buildroot}%{_datadir}/subtitleedit/SubtitleEdit.exe
install -m 0644 -vp %{_builddir}/subtitleedit/System.Net.Http.Extensions.dll %{buildroot}%{_datadir}/subtitleedit/System.Net.Http.Extensions.dll
install -m 0644 -vp %{_builddir}/subtitleedit/System.Net.Http.Primitives.dll %{buildroot}%{_datadir}/subtitleedit/System.Net.Http.Primitives.dll
install -m 0644 -vp %{_builddir}/subtitleedit/UtfUnknown.dll                 %{buildroot}%{_datadir}/subtitleedit/UtfUnknown.dll
install -m 0644 -vp %{_builddir}/subtitleedit/zlib.net.dll                   %{buildroot}%{_datadir}/subtitleedit/zlib.net.dll
install -m 0755 -vd                                                          %{buildroot}%{_datadir}/subtitleedit/Dictionaries
install -m 0644 -vp %{_builddir}/subtitleedit/Dictionaries/*.xml             %{buildroot}%{_datadir}/subtitleedit/Dictionaries
install -m 0755 -vd                                                          %{buildroot}%{_datadir}/subtitleedit/Languages
install -m 0644 -vp %{_builddir}/subtitleedit/Languages/*.xml                %{buildroot}%{_datadir}/subtitleedit/Languages
install -m 0755 -vd                                                          %{buildroot}%{_datadir}/subtitleedit/Ocr
install -m 0644 -vp %{_builddir}/subtitleedit/Ocr/*                          %{buildroot}%{_datadir}/subtitleedit/Ocr
cp -r %{_builddir}/subtitleedit                                              %{buildroot}%{_datadir}
install -m 0755 -vd                                                          %{buildroot}%{_datadir}/pixmaps
install -m 0644 -vp %{_builddir}/subtitleedit.png                            %{buildroot}%{_datadir}/pixmaps/subtitleedit.png
install -m 0755 -vd                                                          %{buildroot}%{_bindir}
install -m 0755 -vp %{S:2}                                                   %{buildroot}%{_bindir}/subtitleedit
install -m 0755 -vd                                                          %{buildroot}%{_datadir}/applications
install -m 0644 -vp %{S:3}                                                   %{buildroot}%{_datadir}/applications/subtitleedit.desktop


%files
%dir %{_datadir}/subtitleedit
%{_datadir}/subtitleedit/*
%{_datadir}/subtitleedit/.PACKAGE-MANAGER
%{_datadir}/pixmaps/subtitleedit.png
%{_bindir}/subtitleedit
%{_datadir}/applications/subtitleedit.desktop


%changelog
* Thu Nov 18 2021 sixg0000d <sixg0000d@gmail.com>
- Initial package
