def sort_objects_by_key(objects, key):
    if not all(isinstance(obj, dict) for obj in objects):
        raise ValueError("All elements must be dictionaries.")
    return sorted(objects, key=lambda x: x.get(key))

class DataSorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        return sort_objects_by_key(self.data, key)

if __name__ == '__main__':
    sample_data = [
        {'title': 'Book', 'year': 2001},
        {'title': 'Magazine', 'year': 1998},
        {'title': 'Journal', 'year': 2015}
    ]
    sorter = DataSorter(sample_data)
    sorted_data = sorter.sort_by_key('year')
    print(sorted_data)