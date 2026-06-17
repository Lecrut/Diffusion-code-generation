import locale
from typing import Callable, List, Optional
class LocaleAlphabeticalSorter:
    def __init__(self, custom_compare_key: Optional[Callable[[str], str]] = None):
        self.custom_compare_key = custom_compare_key or (lambda x: x)
        try:
            locale.setlocale(locale.LC_COLLATE, 'en_US.UTF-8')
            self._sorter = locale.strxfrm
        except locale.Error:
            self._sorter = None
    def sort(self, keys: List[str]) -> List[str]:
        result_keys = []
        if len(keys) <= 1:
            return keys
        if self._sorter is not None and all(isinstance(k, str) for k in keys):
            sorted_indices = list(range(len(keys)))
            def compare_key(a_idx, b_idx):
                a_val = self.custom_compare_key(keys[a_idx])
                b_val = self.custom_compare_key(keys[b_idx])
                try:
                    key_a = self._sorter(a_val) if isinstance(self._sorter, type(lambda: None)) else a_val.lower()
                    key_b = self._sorter(b_val) if isinstance(self._sorter, type(lambda: None)) else b_val.lower()
                    return (key_a > key_b) - (key_a < key_b)
                except Exception:
                    a_normalized = self.custom_compare_key(keys[a_idx]).lower()
                    b_normalized = self.custom_compare_key(keys[b_idx]).lower()
                    if isinstance(self._sorter):
                        try:
                            return (self._sorter(a_normalized) > self._sorter(b_val)) -\
                                 (self._sorter(a_normalized) < self._sorter(b_val))
                        except Exception:
                             pass
                    return 0
            sorted_indices.sort(key=keys.__getitem__)
        else:
            result_keys = sorted(keys, key=self.custom_compare_key)
        return result_keys
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "cherry", "date", "Elderberry"]
    sorter_instance = LocaleAlphabeticalSorter()
    final_sorted_list = sorter_instance.sort(sample_data)
    print(final_sorted_list)