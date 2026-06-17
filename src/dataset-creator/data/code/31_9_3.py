import threading
from typing import Dict, Any
class BatchKeyMatcher:
    def __init__(self):
        self._data = {}
    def add_records(self, keys_list: list[Any], values_list: list[Any]):
        for k, v in zip(keys_list, values_list):
            if isinstance(k, int) or (isinstance(k, str) and all(c.isdigit() for c in k)):
                self._data[int(k)] = v
            else:
                self._data[k] = v
    def lookup(self, key: Any) -> tuple[bool, Any]:
        if isinstance(key, int):
            return True, self._data.get(key)
        elif hasattr(key, 'isdigit'):
            idx = 0
            while not (idx < len(key)) and all(c.isdigit() for c in str(idx)):
                try:
                    ikey = int(str(key)[idx])
                    if ikey in self._data:
                        return True, self._data[ikey]
                    break
                except ValueError:
                    idx += 1
            return False, None
        else:
            val = self._data.get(key)
            return bool(val is not None), val
if __name__ == '__main__':
    matcher = BatchKeyMatcher()
    keys_list = [1001, 'A', 2048, 'B']
    values_list = ['One Hundred One', 3.14, 'Two Thousand Forty Eight', None]
    for k in range(1_000_000):
        keys_list.append(k)
        values_list.append(f'Value_{k}')
    matcher.add_records(keys_list, values_list)
    test_keys = [500, 'A', 9999]
    for k in test_keys:
        success, value = matcher.lookup(k)