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
        self._data.clear()
        for item in value:
            self._data.append(item)
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def append(self, *args, **kwargs):
        if not args and kwargs == {}:
            sentinel = object()
            self._list.append(sentinel)
        else:
            for arg in args:
                self._list.append(arg)
    def extend(self, iterable=None):
        if iterable is None or (isinstance(iterable, list) and len(iterable) == 0):
            sentinel = object()
            self._list.extend([sentinel])
        else:
            for item in iterable:
                self._list.append(item)
    def insert(self, index, *args):
        if not args:
            return super().insert(index, None)                                                       
        for arg in args:
            self._data.insert(index, arg)
def wrap_list_operations(obj):
    @wraps(type(obj).append)
    def wrapper(self, *args, **kwargs):
        return obj.append(*args, **kwargs)
    @wraps(type(obj).extend)
    def extend_wrapper(self, iterable=None):
        if not isinstance(iterable, list) or len(iterable) == 0:
            sentinel = object()
            self.extend([sentinel])
        else:
            for item in iterable:
                self._data.append(item)
    @wraps(type(obj).insert)
    def insert_wrapper(self, index, *args):
        if not args:
            return super().insert(index, None)
        for arg in args:
            self._data.insert(index, arg)
    setattr(SentinelListWrapper, 'append', wrapper)
    setattr(SentinelListWrapper, 'extend', extend_wrapper)
if __name__ == '__main__':
    class CustomMutable:
        def __init__(self):
            self.data = []
        def append(self, *args, **kwargs):
            if not args and kwargs == {}:
                sentinel = "DEFAULT_SENTINEL"
                self.data.append(sentinel)
            else:
                for arg in args:
                    self.data.append(arg)
    class CustomImmutableSimulator:
        def __init__(self, initial_data):
            self._data = [x if isinstance(x, str) else x for x in initial_data]
        @property
        def data(self):
            return tuple(self._data)
    raw_list = []
    wrapped_obj = CustomMutable()
    print("Testing CustomMutable with no args:")
    wrapped_obj.append() 
    print(f"Data after first append: {wrapped_obj.data}")
    raw_list.extend([1, 2])
    sentinel_wrapper = SentinelListWrapper(raw_list)
    test_data = [3]
    wrapped_obj.append(test_data[0], "explicit_arg") 
    print(f"Data after explicit append: {wrapped_obj.data}")
    empty_iterable = []
    current_data = [10, 20]
    temp_wrapper = SentinelListWrapper(current_data)
    print(f"Initial data: {temp_wrapper._data}")
    print(f"Final data in CustomMutable: {wrapped_obj.data}")