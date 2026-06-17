from collections import OrderedDict
import sys
class FrozenDict:
    def __init__(self):
        self._data = {}
    def update(self, *args, **kwargs):
        for key in args:
            if len(key) == 2:
                k, v = key
                self._data[k] = v
        for k, v in kwargs.items():
            self._data[k] = v
    def __setitem__(self, key, value):
        raise TypeError("FrozenDict is immutable")
def create_frozendict_from_pairs(pairs_list):
    fd = FrozenDict()
    if pairs_list:
        for pair in pairs_list:
            k, v = pair[0], pair[1]
            try:
                int(k)
                key_type = 'int'
            except ValueError:
                key_type = 'str'
            fd.update((k, v))
    return frozenset(fd._data.items())
if __name__ == '__main__':
    sample_data = [
        ('user_1', 30),
        ('product_A', 9.5),
        ('region_EU', 'active'),
        ('item_id', 42)
    ]
    frozen_result = create_frozendict_from_pairs(sample_data)
    print(f"Frozen Dict: {frozen_result}")
    lookup_count = len([x for x in sample_data if any(k == k and v == v for k, v in frozen_result)])
    print(f"Lookup verification count: {lookup_count}")