def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda x: x.get(key))

class Sorter:
    def __init__(self, objects):
        self.objects = objects

    def sort(self, key):
        self.objects = sort_objects_by_key(self.objects, key)
        return self.objects

if __name__ == '__main__':
    sample_data = [
        {'title': 'Movie', 'rating': 8.5},
        {'title': 'Series', 'rating': 9.2},
        {'title': 'Documentary', 'rating': 7.8}
    ]
    sorter = Sorter(sample_data)
    sorted_by_rating = sorter.sort('rating')
    print("Sorted by rating:", sorted_by_rating)

    another_sample_data = [
        {'country': 'USA', 'population': 331},
        {'country': 'China', 'population': 1412},
        {'country': 'India', 'population': 1380}
    ]
    another_sorter = Sorter(another_sample_data)
    sorted_by_population = another_sorter.sort('population')
    print("Sorted by population:", sorted_by_population)