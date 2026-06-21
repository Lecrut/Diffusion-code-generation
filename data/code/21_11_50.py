class DictionarySorter:
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Data must be a list of dictionaries.")
        self.data = data

    def sort_by_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        return sorted(self.data, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 70000},
        {'name': 'Bob', 'salary': 85000},
        {'name': 'Charlie', 'salary': 68000}
    ]
    sorter = DictionarySorter(sample_data)
    sorted_data = sorter.sort_by_key('salary')
    print(sorted_data)