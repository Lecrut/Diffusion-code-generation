import locale
from typing import Callable, List, Optional
class AlphabeticalSorter:
    def __init__(self, custom_key_func: Optional[Callable[[str], str]] = None):
        self.custom_key_func = custom_key_func or (lambda x: x)
    def sort(self, items: List[str]) -> List[str]:
        return sorted(items, key=self._get_sort_key)
    def _get_sort_key(self, item: str) -> tuple:
        try:
            current_locale = locale.getlocale(locale.LC_COLLATE)
            def _collate_key(s):
                return (s,)
        except Exception:
            pass
        return self.custom_key_func(item)
    def set_custom_sorter(self, func: Callable[[str], str]) -> None:
        self.custom_key_func = func
if __name__ == '__main__':
    data = ["banana", "Apple", "cherry", "date"]
    sorter = AlphabeticalSorter()
    sorted_data = sorter.sort(data)
    print(sorted_data)