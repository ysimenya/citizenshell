from .abstractshell import AbstractShell

class AbstractRemoteShell(AbstractShell):

    def __init__(self, target, *args, **kwargs):
        self._target = target
        super(AbstractRemoteShell, self).__init__(*args, **kwargs)
        self._connected = False

    def __repr__(self):
        return "%s(id=%s,target=%s)" % (self.__class__.__name__, repr(self._id), repr(self._target))

    def is_connected(self):
        return self._connected

    def connect(self):
        if not self._connected:
            self.log_oob("connecting to '%s'..." % self._target)
            self.do_connect()
            self._connected = True
            self.log_oob("connected!")

    def disconnect(self):
        if self._connected:
            self.log_oob("disconnected from '%s'..." % self._target)
            self.do_disconnect()
            self.log_oob("disconnected!")

    def do_connect(self):
        raise NotImplementedError("this method should be implemented by subclass")

    def do_disconnect(self):
        raise NotImplementedError("this method should be implemented by subclass")


    