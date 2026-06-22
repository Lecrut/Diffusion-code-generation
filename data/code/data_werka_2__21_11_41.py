class DictSorter:
    def __init__(self, dicts):
        if not isinstance(dicts, list) or not all(isinstance(d, dict) for d in dicts):
            raise ValueError("Input must be a list of dictionaries.")
        self.dicts = dicts

    def sort_by_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        return sorted(self.dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'height': 165},
        {'name': 'Bob', 'height': 180},
        {'name': 'Charlie', 'height': 175}
    ]
    sorter = DictSorter(sample_dicts)
    sorted_dicts = sorter.sort_by_key('height')
    print(sorted_dicts)