import threading

class Singleton:
    _instance_lock = threading.Lock()
    _instance = None
    _data = {}

    def __new__(cls):
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def set_value(self, key, value):
        with self._instance_lock:
            self._data[key] = value

    def get_value(self, key):
        with self._instance_lock:
            return self._data.get(key, None)

if __name__ == '__main__':
    singleton = Singleton()
    singleton.set_value('pi', 3.14159)
    print(singleton.get_value('pi'))