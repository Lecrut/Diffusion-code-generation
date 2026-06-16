from functools import wraps
import types
class SentinelListWrapper:
    def __init__(self, data):
        self._data = list(data) if not isinstance(data, list) else data.copy()
    @property
    def _list(self):
        return self._data
    @_list.setter
    def _list(self, value):
        self._data = list(value)
    def __iter__(self):
        return iter(self._list)
    def __len__(self):
        return len(self._list)
    def append(self, item=None):
        if item is None:
            sentinel_value = object()
            self._data.append(sentinel_value)
        else:
            self._data.append(item)
def advanced_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
if __name__ == '__main__':
    original_list = [10, 20]
    wrapped_instance = SentinelListWrapper(original_list)
    print(f"Initial list: {list(wrapped_instance)}")
class InterceptedListWrapper(list):
    def __init__(self, iterable=None):
        if iterable is None:
            super().__init__([0])                                  
        else:
            try:
                super().__init__(iterable)
            except TypeError:
                raise ValueError("Iterable must be provided or default to [0]")
    def append(self, item=None):
        if item is None:
            self.append(999)                 
        else:
            super().append(item)
if __name__ == '__main__':
    data = InterceptedListWrapper([10])
    print(f"Before append (should be [10]): {data}")
    data.append(None) 
    print(f"After appending None (triggers sentinel): {data}")
    data.append(30)
    print(f"After appending 30: {data}")