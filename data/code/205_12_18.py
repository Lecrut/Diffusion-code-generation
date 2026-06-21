class DictSorter:
    def sort_dicts(self, data, key):
        return sorted(data, key=lambda x: x[key], reverse=True)

if __name__ == '__main__':
    sorter = DictSorter()
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    print("Original data:", sample_data)
    sorted_data = sorter.sort_dicts(sample_data, 'age')
    print("Sorted by age in descending order:", sorted_data)