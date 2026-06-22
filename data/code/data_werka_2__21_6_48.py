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
    sorted_by_year = sorter.sort_by_key('year')
    print("Sorted by year:", sorted_by_year)

    sample_data_2 = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorter_2 = ObjectSorter(sample_data_2)
    sorted_by_age = sorter_2.sort_by_key('age')
    print("Sorted by age:", sorted_by_age)