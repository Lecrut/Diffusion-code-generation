import re
def normalize_name(name: str) -> str:
    name = name.strip()
    return ''.join(c.lower() for c in name if not c.isalnum())
class AnimalTracker:
    def __init__(self):
        self._database = {}
    def add_from_iterable(self, items):
        normalized_list = [normalize_name(item) for item in items]
        unique_items = list(dict.fromkeys(normalized_list))
        return set(unique_items)
    def get_all_animals(self) -> set:
        return self._database.keys()
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data_1 = ['Lion', 'Tiger', 'LEO']
    sample_data_2 = {'tiger', 'lion', 'Bears'}
    added_animals = list(tracker.add_from_iterable(sample_data_1))
    added_animals.extend(list(tracker.add_from_iterable(sample_data_2)))
    print(f"Total unique animals tracked: {len(tracker.get_all_animals())}")