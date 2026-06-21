class DictSorter:
    def __init__(self, dicts):
        self.dicts = dicts

    def sort_by_key(self, key):
        return sorted(self.dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78}
    ]
    sorter = DictSorter(sample_dicts)
    sorted_dicts = sorter.sort_by_key('score')
    print(sorted_dicts)