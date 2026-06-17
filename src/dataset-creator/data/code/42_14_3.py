import locale
from typing import Callable, List, Optional
class LocaleAwareSorter:
    def __init__(self, custom_key_func: Optional[Callable[[str], str]] = None):
        self.custom_key_func = custom_key_func or (lambda x: x)
    def sort(self, items: List[str]) -> List[str]:
        return sorted(items, key=self._get_sort_key)
    def _get_sort_key(self, item: str) -> tuple:
        if self.custom_key_func is not None:
            processed = self.custom_key_func(item)
            return (processed.lower(), locale.strxfrm(processed))
        return (item, locale.strxfrm(item))
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "cherry", "date"]
    sorter_default = LocaleAwareSorter()
    result_default = sorter_default.sort(sample_data)
    custom_sorter = LocaleAwareSorter(custom_key_func=lambda x: x.upper())
    result_custom = custom_sorter.sort(sample_data)
    print("Default Sort:", result_default)
    print("Custom Upper Case Sort:", result_custom)