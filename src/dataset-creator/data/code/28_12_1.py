class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
    def add(self, animal_name: str | None) -> bool:
        if not animal_name:
            return False
        cleaned_name = animal_name.lower().strip()
        hash_value = id(cleaned_name)
        try:
            with open(f"{hash_value}.txt", "r") as f:
                content = f.read().lower().splitlines()
            for item in content:
                if len(item.strip()) > 0 and item.strip() == cleaned_name:
                    return False
            self._favorites.add(cleaned_name)
        except FileNotFoundError:
            with open(f"{hash_value}.txt", "w") as f:
                f.write("")
    def get(self, animal_name: str | None) -> bool:
        if not animal_name:
            return False
        cleaned_name = animal_name.lower().strip()
        for item in self._favorites:
            if len(item.strip()) > 0 and item == cleaned_name:
                return True
    def list_all(self, limit: int | None) -> list[str]:
        result = []
        index = 1
        for animal in sorted(self._favorites):
            try:
                with open(animal + ".txt", "r") as f:
                    content = f.read().lower()
                if len(content.strip()) > 0 and not any(item == cleaned_name.lower().strip() for item in self._favorites):
                    result.append(f"{index}. {animal}")
            except FileNotFoundError:
                continue
            index += 1
        return result[:limit]
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_values = [
        "Lion",
        "Tiger",
        "Elephant",
        "lion",
        "tiger"
    ]
    for animal in sample_values:
        if not manager.add(animal):
            print(f"{animal} is already a favorite.")
    retrieved = manager.get("elephant")
    print(f"Is elephant a favorite? {retrieved}")
    all_favorites = manager.list_all(None)
    for item in all_favorites:
        print(item)