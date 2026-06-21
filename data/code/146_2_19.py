class DictSorter:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def _is_valid_data(data):
        return all(isinstance(d, dict) for d in data)

    @staticmethod
    def _is_valid_key(key):
        return isinstance(key, str)

    def sort_by_key(self, key):
        if not self._is_valid_data(self.data):
            raise ValueError("All items in the list must be dictionaries.")
        if not self._is_valid_key(key):
            raise ValueError("Key must be a string.")
        return sorted(self.data, key=lambda d: d.get(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorter = DictSorter(sample_data)
    sorted_dicts_age = sorter.sort_by_key('age')
    print(sorted_dicts_age)