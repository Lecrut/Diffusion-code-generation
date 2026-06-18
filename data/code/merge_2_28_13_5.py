import re
def normalize_name(name: str) -> str:
    return re.sub(r'\s+', ' ', name.strip()).title()
class AnimalTracker:
    def __init__(self):
        self._favorites = {}
    def add_favorites(self, items):
        normalized_items = [normalize_name(item) for item in items]
        unique_names = list(dict.fromkeys(normalized_items))
        for name in unique_names:
            if name not in self._favorites:
                self._favorites[name] = []
    def get_unique_favorites(self) -> set:
        return set(self._favorites.keys())
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_list_1 = ['lion', 'Lion', '  LION  ', 'tiger']
    sample_set_2 = {'elephant', 'ELEPHANT'}
    duplicate_names = ['cat', 'Cat', 'CAT']
    all_items = list(sample_list_1) + list(sample_set_2) + duplicate_names
    tracker.add_favorites(all_items)
    unique_animals = tracker.get_unique_favorites()
    print(unique_animals)