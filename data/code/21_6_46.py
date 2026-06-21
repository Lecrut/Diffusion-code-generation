def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda x: x.get(key))

class ObjectSorter:

    def __init__(self, objects):
        self.objects = objects

    def sort_by(self, key):
        return sorted(self.objects, key=lambda x: x.get(key))
if __name__ == '__main__':
    sample_data = [{'title': 'Movie', 'rating': 8.5}, {'title': 'TV Show', 'rating': 7.9}, {'title': 'Documentary', 'rating': 9.2}]
    sorted_data_function = sort_objects_by_key(sample_data, 'rating')
    print('Sorted by rating using function:', sorted_data_function)
    sorter = ObjectSorter(sample_data)
    sorted_data_class = sorter.sort_by('rating')
    print('Sorted by rating using class:', sorted_data_class)