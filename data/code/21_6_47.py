class ObjectSorter:
    def __init__(self, objects):
        if not all(isinstance(obj, dict) for obj in objects):
            raise ValueError("All elements must be dictionaries.")
        self.objects = objects

    def sort_by_key(self, key):
        return sorted(self.objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'title': 'Book', 'year': 2001},
        {'title': 'Magazine', 'year': 1998},
        {'title': 'Journal', 'year': 2015}
    ]
    sorter = ObjectSorter(sample_data)
    sorted_data = sorter.sort_by_key('year')
    print(sorted_data)