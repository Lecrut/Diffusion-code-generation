class DictSorter:
    def sort_dicts(self, data, key):
        return sorted(data, key=lambda x: x[key], reverse=True)

if __name__ == '__main__':
    sorter = DictSorter()
    sample_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
    print("Original list:", sample_list)
    sorted_by_age = sorter.sort_dicts(sample_list, 'age')
    print("Sorted by age:", sorted_by_age)
    sorted_by_name = sorter.sort_dicts(sample_list, 'name')
    print("Sorted by name:", sorted_by_name)