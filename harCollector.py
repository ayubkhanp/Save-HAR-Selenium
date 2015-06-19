import sys, re, os, time, datetime, urllib2
import subprocess, hashlib
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def harCollector(url):
    fireBugPath = '~/HarCollector/firebug-2.0.11.xpi';
    netExportPath = '~/HarCollector/netExport-0.9b7.xpi';
    fireStarterPath = '~/HarCollector/fireStarter-0.1a6.xpi';
    binary = FirefoxBinary('/usr/bin/firefox');

    # firefox profile file
    profile = webdriver.firefox.firefox_profile.FirefoxProfile();
    profile.add_extension( fireBugPath);
    profile.add_extension(netExportPath);
    profile.add_extension(fireStarterPath);

    #firefox preferences
    profile.set_preference("app.update.enabled", False)
    profile.native_events_enabled = True
    #profile.set_preference("webdriver.log.file", "/home/akhan/Desktop/HarCollector/webFile.txt")
    profile.set_preference("extensions.firebug.DBG_STARTER", True);

    profile.set_preference("extensions.firebug.currentVersion", "2.0.11");
    profile.set_preference("extensions.firebug.addonBarOpened", True);
    profile.set_preference("extensions.firebug.addonBarOpened", True);
    profile.set_preference('extensions.firebug.consoles.enableSite', True)


    profile.set_preference("extensions.firebug.console.enableSites", True);
    profile.set_preference("extensions.firebug.script.enableSites", True);
    profile.set_preference("extensions.firebug.net.enableSites", True);
    profile.set_preference("extensions.firebug.previousPlacement", 1);
    profile.set_preference("extensions.firebug.allPagesActivation", "on");
    profile.set_preference("extensions.firebug.onByDefault", True);
    profile.set_preference("extensions.firebug.defaultPanelName", "net");

    #set net export preferences
    profile.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True);
    profile.set_preference("extensions.firebug.netexport.autoExportToFile", True);
    profile.set_preference("extensions.firebug.netexport.saveFiles", True);

    profile.set_preference("extensions.firebug.netexport.autoExportToServer", False);
    profile.set_preference("extensions.firebug.netexport.Automation", True);
    profile.set_preference("extensions.firebug.netexport.showPreview", False);
    profile.set_preference("extensions.firebug.netexport.pageLoadedTimeout", 15000);
    profile.set_preference("extensions.firebug.netexport.timeout", 10000);

    profile.set_preference("extensions.firebug.netexport.defaultLogDir", "~/HarCollector/Storage/");
    profile.update_preferences();

    browser = webdriver.Firefox(firefox_profile=profile,firefox_binary=binary);
    time.sleep(3);
    browser.get(url); #load the url in firefox
    time.sleep(10);
    browser.quit()

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in f:
            harCollector(line)
