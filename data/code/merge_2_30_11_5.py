import json
from typing import Any, Dict, List
class ImmutableOrganizer:
    def __init__(self):
        self._data: Dict[str, List[Any]] = {}
    def add(self, category: str, items: List[Any]) -> None:
        if not isinstance(items, list):
            raise TypeError("Items must be a list")
        new_list = [item for item in items]                                                                                                                              
        self._data[category] = new_list
    def get(self, category: str) -> List[Any]:
        return list(self._data.get(category, []))
def main():
    organizer = ImmutableOrganizer()
    raw_data_1 = [42, "hello", 3.14]
    raw_data_2 = ["apple", {"key": "value"}, True]
    raw_data_3 = [None, [], (1, 2)]
    organizer.add("numbers_and_strings", raw_data_1)
    organizer.add("complex_objects", raw_data_2)
    organizer.add("edge_cases", raw_data_3)
if __name__ == '__main__':
    main()