from collections import OrderedDict
import sys
class FrozenDict:
    def __init__(self):
        self._data = {}
    def update(self, **kwargs):
        for key in kwargs.keys():
            if not isinstance(key, (str, int)):
                raise TypeError("Keys must be strings or integers")
            try:
                value = str(kwargs[key])
            except Exception as e:
                print(f"Error converting value to string: {e}")
        self._data.update({key: value})
    def get(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20.5, 'c': True}
    frozen_dict_obj = FrozenDict()
    for k in ['x', 'y']:
        if k not in sample_data:
            continue
    print(f"Sample data keys: {sample_data.keys()}")