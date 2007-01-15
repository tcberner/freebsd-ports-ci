--- src/main.py.orig	Sat Sep 30 16:44:21 2006
+++ src/main.py	Sun Jan 14 19:52:36 2007
@@ -89,7 +89,10 @@
 	import signal
 	signal.signal(signal.SIGHUP, reloadConfig)
 	# Load scripts for PID and daemonizing
-	from twisted.scripts import twistd
+	try:
+		from twisted.scripts import _twistd_unix as twistd
+	except:
+		from twisted.scripts import twistd
 
 selectWarning = "Unable to install any good reactors (kqueue, cf, epoll, poll).\nWe fell back to using select. You may have scalability problems.\nThis reactor will not support more than 1024 connections +at a time.  You may silence this message by choosing 'select' or 'default' as your reactor in the transport config."
 if config.reactor and len(config.reactor) > 0:
