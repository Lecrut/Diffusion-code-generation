import re
class AnimalTracker:
    def _normalize_name(self, name):
        return ' '.join(word.capitalize() for word in re.split(r'[-\s]+', str(name).strip())) if name else ''
    def add_animals(self, source_list=None):
        animals = set()
        if isinstance(source_list, list) and len(source_list) > 0:
            [animals.add(a.strip()) for a in source_list]
        elif isinstance(source_list, set) and len(source_list) > 0:
            animals.update([a.strip() for a in source_list])
        return {self._normalize_name(name): name for name in animals}
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data_1 = ['lion', 'Lioness', 'lions']
    sample_data_2 = {'tiger', 'TIGER'}
    result_set = set(sample_data_1 + list(sample_data_2))
    normalized_map = tracker.add_animals(result_set)
    print("Unique Normalized Animals:")
    for animal in sorted(normalized_map.keys()):
        print(f"{animal}: {normalized_map[animal]}")