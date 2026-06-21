class DictSorter:
    def sort_dicts(self, data, key):
        return sorted(data, key=lambda x: x[key], reverse=True)

if __name__ == '__main__':
    sorter = DictSorter()
    sample_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
    print("Original list:", sample_list)
    sorted_list = sorter.sort_dicts(sample_list, 'age')
    print("Sorted list by age in descending order:", sorted_list)

    sample_list_2 = [{'product': 'Apple', 'price': 1.5}, {'product': 'Banana', 'price': 0.75}, {'product': 'Cherry', 'price': 2.0}]
    print("\nOriginal list:", sample_list_2)
    sorted_list_2 = sorter.sort_dicts(sample_list_2, 'price')
    print("Sorted list by price in descending order:", sorted_list_2)