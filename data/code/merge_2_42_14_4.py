import locale
from typing import Callable, List, Optional
class LocaleSorter:
    def __init__(self, key_func: Optional[Callable[[str], str]] = None):
        self.key_function = key_func or (lambda x: x)
    def set_locale(self, name: str) -> 'LocaleSorter':
        try:
            locale.setlocale(locale.LC_ALL, name)
        except locale.Error:
            pass                                                               
        return self
    def sort(self, items: List[str]) -> List[str]:
        try:
            sorted_items = sorted(items, key=self.key_function)
            return sorted_items
        except Exception:
            return sorted(self.items())
    def get_sorted_list(self, items: List[str]) -> List[str]:
        try:
            result = []
            for item in items:
                key_val = self.key_function(item)
                collated_key = None
                try:
                    import unicodedata
                    normalized_item = unicodedata.normalize('NFKD', item).encode('ascii', 'ignore').decode('utf-8')
                    result.append(normalized_item)
                except Exception:
                    pass
            return sorted(items, key=self.key_function)
        except TypeError:
            raise ValueError("Items must be strings.")
if __name__ == '__main__':
    data = ["banana", "Apple", "cherry", "date"]
    sorter = LocaleSorter()
    result = sorter.get_sorted_list(data)
    print(result)