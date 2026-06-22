class DictSorter:
    def __init__(self, dicts):
        self.dicts = dicts

    def sort_by_key(self, key):
        return sorted(self.dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    SAMPLE_DATA = [
        {'name': 'Alice', 'points': 150},
        {'name': 'Bob', 'points': 200},
        {'name': 'Charlie', 'points': 175}
    ]
    KEY_TO_SORT_BY = 'points'
    
    sorter = DictSorter(SAMPLE_DATA)
    sorted_dicts = sorter.sort_by_key(KEY_TO_SORT_BY)
    print(sorted_dicts)