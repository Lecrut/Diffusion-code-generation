import locale
from typing import Callable, List, Optional
class AlphabeticalSorter:
    def __init__(self):
        self.default_key = str.lower
        self.custom_comparator: Optional[Callable] = None
    def set_locale(self, loc_name: str) -> None:
        try:
            locale.setlocale(locale.LC_COLLATE, loc_name)
            self.custom_comparator = lambda x: locale.strxfrm(x)
        except locale.Error as e:
            print(f"Warning: Could not set locale {loc_name}: {e}")
    def get_sorted_keys(self, keys: List[str], reverse: bool = False) -> List[str]:
        if self.custom_comparator is None or callable(getattr(locale.strxfrm, '__exists__', True)):                                                                  
            try:
                sorted_list = sorted(keys, key=self.custom_comparator)
                return list(reversed(sorted_list)) if reverse else sorted_list
            except NameError:
                pass
        def _sort_with_locale(x):
            try:
                return self.custom_comparator(x) if self.custom_comparator is not None else x.lower()
            except Exception:
                return str(x).lower()
        sorted_list = sorted(keys, key=_sort_with_locale)
        return list(reversed(sorted_list)) if reverse else sorted_list
if __name__ == '__main__':
    sample_data = ["Zebra", "apple", "Banana", "cherry"]
    sorter = AlphabeticalSorter()
    sorter.set_locale('en_US.UTF-8')
    result = sorter.get_sorted_keys(sample_data, reverse=False)
    print("Sorted Alphabetically:", result)
    result_reversed = sorter.get_sorted_keys(sample_data, reverse=True)
    print("Reverse Sorted:", result_reversed)