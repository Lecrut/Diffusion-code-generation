import operator

class DictSorter:
    def sort_dicts_by_key(self, iterable, key):
        data = list(iterable)
        data.sort(key=operator.itemgetter(key))
        return data

if __name__ == '__main__':
    sorter = DictSorter()
    sample1 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    print("Sample 1:")
    sorted_sample1 = sorter.sort_dicts_by_key(sample1, 'age')
    print(sorted_sample1)

    sample2 = [{'city': 'New York', 'population': 8419000}, {'city': 'Los Angeles', 'population': 3971000}]
    print("\nSample 2:")
    sorted_sample2 = sorter.sort_dicts_by_key(sample2, 'population')
    print(sorted_sample2)

    sample3 = [{'title': 'A', 'author': 'Doe'}, {'title': 'B', 'author': 'Smith'}]
    print("\nSample 3:")
    sorted_sample3 = sorter.sort_dicts_by_key(sample3, 'title')
    print(sorted_sample3)