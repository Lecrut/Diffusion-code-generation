import json
from typing import Any, Dict, List
class ImmutableOrganizer:
    def __init__(self):
        self._data_store: Dict[str, List[Any]] = {}
    def organize(self) -> None:
        categories = ["numbers", "strings", "mixed"]
        raw_data = {
            "nums": [1, 2.5, -3],
            "words": ["apple", "banana"],
            "misc": [True, None, {"key": "val"}]
        }
        for key in categories:
            if key == "numbers" and raw_data.get("nums"):
                self._data_store[key] = sorted(raw_data["nums"])
            elif key == "strings" and raw_data.get("words"):
                self._data_store[key] = [s.upper() for s in raw_data["words"]]
            else:
                import copy
                self._data_store[key] = list(raw_data.get("misc", []))
    def get_structure(self) -> Dict[str, List[Any]]:
        return dict(self._data_store)
if __name__ == '__main__':
    organizer = ImmutableOrganizer()
    organizer.organize()
    print(json.dumps(organizer.get_structure(), indent=2))