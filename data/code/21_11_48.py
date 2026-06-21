class DictSorter:
    def __init__(self, data):
        self._validate_input(data)
        self.data = data

    def _validate_input(self, data):
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Input must be a list of dictionaries.")

    def sort_by_key(self, key):
        self._validate_key(key)
        return sorted(self.data, key=lambda x: x.get(key, 0), reverse=True)

    def _validate_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'grade': 'B'},
        {'name': 'Bob', 'grade': 'A'},
        {'name': 'Charlie', 'grade': 'C'}
    ]
    sorter = DictSorter(sample_dicts)
    sorted_dicts = sorter.sort_by_key('grade')
    print(sorted_dicts)