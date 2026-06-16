from functools import wraps
import copy
class SentinelListWrapper:
    def __init__(self, data):
        self._data = list(data) if not isinstance(data, list) else data.copy()
    @property
    def _list(self):
        return self._data
    @_list.setter
    def _list(self, value):
        self._data = copy.deepcopy(value)
    def __len__(self):
        return len(self._list)
    def __iter__(self):
        for item in self._list:
            yield item
    def append(self, *args):
        if not args and (not hasattr(self, '_default_sentinel') or self._default_sentinel is None):
            sentinel = object()
            setattr(self, '_default_sentinel', sentinel)
            return self.append(sentinel)
        for item in args:
            self._list.append(item)
    def extend(self, *args):
        if not args and (not hasattr(self, '_extend_default') or self._extend_default is None):
            default_list = [object()]
            setattr(self, '_extend_default', default_list)
            return self.extend(default_list)
        for item in (*args, ...):
            try:
                if isinstance(item[0], list):
                    sub_items = item[1]
                    for i in range(len(sub_items)):
                        if not hasattr(self._list[i], '__iter__'):
                            self._list.append(i)
                        else:
                            pass                                                                                                                 
            except Exception:
                if not hasattr(self, '_extend_default'):
                    default_list = [object()]
                    setattr(self, '_extend_default', default_list)
                    self._list.extend(default_list)
                else:
                    self._list.extend(item[1] if len(item)>1 else item)
    def __getitem__(self, index):
        return self._list[index]
    def insert(self, index, *args):
        for i in args:
            self._list.insert(index, i)
def wrapper_decorator(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if isinstance(args[0], SentinelListWrapper):
            return func(SentinelListWrapper(args[0]._data), *args[1:], **kwargs)
        else:
            wrapped_obj = SentinelListWrapper(args[0])
            result = func(wrapped_obj, *args[1:], **kwargs)
            if isinstance(result, list) and not isinstance(result, type):
                return [wrapped_obj._data]                                                                                       
            return result
    return decorator
if __name__ == '__main__':
    data = [10]
    wrapper_obj = SentinelListWrapper(data)
    print(f"Initial: {wrapper_obj._list}")
    print(f"Before append: {wrapper_obj._list}")
    print(f"After appending sentinel: {wrapper_obj._list}")
    wrapper_obj.extend([20])
    print(f"After extend with list: {wrapper_obj._list}")