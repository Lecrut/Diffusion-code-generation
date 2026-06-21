class DictSorter:
    DEFAULT_KEY = 'age'

    @staticmethod
    def _validate_dicts(dicts):
        if not isinstance(dicts, list) or not all(isinstance(d, dict) for d in dicts):
            raise ValueError("Input must be a list of dictionaries.")

    @staticmethod
    def _validate_key(key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")

    def __init__(self, dicts):
        self._validate_dicts(dicts)
        self.dicts = dicts

    def sort_by_key(self, key=None):
        if key is None:
            key = DictSorter.DEFAULT_KEY
        self._validate_key(key)
        return sorted(self.dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorter = DictSorter(sample_dicts)
    sorted_dicts = sorter.sort_by_key()
    print(sorted_dicts)