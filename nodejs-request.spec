%{?scl:%scl_package nodejs-request}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}
 
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-request
Version:    2.72.0
Release:    1%{?dist}
Summary:	Simplified HTTP request client
License:	ASL 2.0
URL:		https://github.com/request/request
Source0:	http://registry.npmjs.org/request/-/request-%{version}.tgz
BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch
BuildRequires:	%{?scl_prefix}nodejs-devel

%description
Request is designed to be the simplest way possible to make HTTP calls. It
supports HTTPS and follows redirects by default.

You can stream any response to a file stream. You can also stream a file to a
PUT or POST request.  It also supports a few simple server and proxy functions.

%prep
%setup -q -n package

%nodejs_fixdep har-validator

#remove bundled modules
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/request
cp -pr lib/ *.js package.json %{buildroot}%{nodejs_sitelib}/request

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
node tests/run.js
%endif

%files
%{nodejs_sitelib}/request
%doc README.md
%license LICENSE

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.72.0-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-7
- rebuilt

* Fri Sep 11 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-6
- Add lib/ to %%install

* Thu Aug 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-5
- Rebuilt

* Thu Aug 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-4
- Modified macros

* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-3
- Add %%nodejs_fixdep macros

* Mon Aug 10 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-2
- Fix ExclusiveArch

* Wed Jul 15 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.42.0-1
- New upstream release
- minor changes

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 2.25.0-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.25.0-1
- new upstream release 2.25.0

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.21.0-1
- new upstream release 2.21.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-5
- restrict to compatible arches

* Tue May 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.16.6-4
- make versioned dependency on npm(qs) less specific
- add %%check

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-3
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.16.6-3
- Add support for software collections

* Wed Apr 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-2
- fix versions for newly added dependencies

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-1
- new upstream release 2.16.6
- cookie library now unbundled upstream

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.14.0-1
- new upstream release 2.14.0

* Tue Jan 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-5
- actually make patch work
- fix typo

* Mon Jan 28 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-4
- actually apply patch
- manually create dependency link to private module tobi-cookie

* Thu Jan 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-3
- unbundle cookie stuff

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-2
- add missing build section
- improve description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-1
- new upstream release 2.12.0
- clean up for submission

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.202-1
- New upstream release 2.9.202

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.153-1
- new upstream release 2.9.153

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.151-1
- new upstream release 2.9.151

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.100-1
- new upstream release 2.9.100

* Thu Dec 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.9-1
- new upstream release 2.2.9

* Mon Nov 07 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.0-1
- new upstream release 2.2.0
- adds node v0.6 support

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-2.20110928.646c80dgit
- npm needs a newer git snapshot (apparently upstream moved to rolling release anyway)

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- initial package
