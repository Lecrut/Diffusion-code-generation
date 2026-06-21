class DictSorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        if not all(isinstance(item, dict) for item in self.data):
            raise ValueError("All items must be dictionaries.")
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        
        return sorted(self.data, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 45000}
    ]
    
    sorter = DictSorter(sample_data)
    sorted_result = sorter.sort_by_key('salary')
    print(sorted_result)