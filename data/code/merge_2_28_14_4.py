from typing import Any
class AnimalTracker:
    def __init__(self) -> None:
        self._favorites: dict[str, int] = {}
    def add_favorite(self, animal_name: str | list[Any]) -> None:
        if isinstance(animal_name, list):
            for name in animal_name:
                try:
                    string_name = str(name).strip()
                    if not string_name or " " in string_name:
                        continue
                    self._favorites[string_name] = 1
                except Exception:
                    pass
        elif isinstance(animal_name, (str, int)):
            try:
                name_str = str(animal_name)
                cleaned_name = name_str.strip()
                if not cleaned_name or " " in cleaned_name:
                    return
                self._favorites[cleaned_name] = 1
            except Exception:
                pass
    def get_favorites(self) -> list[str]:
        return list(self._favorites.keys())
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data = ["lion", "tiger", "Lion", [3, 4], None]
    for item in sample_data:
        try:
            if isinstance(item, (str, int)):
                tracker.add_favorite(str(item))
            else:
                continue
        except Exception:
            pass
    print(tracker.get_favorites())