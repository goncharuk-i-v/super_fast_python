"""
There are two ways
to specify the activity: by passing a callable object to the constructor, or
by overriding the run() method in a subclass.
"""

# SuperFastPython.com
# example of extending the Thread class
from time import sleep
from threading import Thread


# custom thread class
class CustomThread(Thread):
    # override the run method in subclass
    def run(self):
        # block for a moment
        sleep(2)
        # display a message
        print('This is coming from another thread')


# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
print('Main thread finished')
