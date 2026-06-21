def sort_dicts_by_key_value(dict_list, key):
    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

class DictSorter:
    def __init__(self, dict_list, key):
        self.dict_list = dict_list
        self.key = key

    def sort(self):
        return sort_dicts_by_key_value(self.dict_list, self.key)

if __name__ == '__main__':
    data1 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
    sorter = DictSorter(data1, 'age')
    print("Original list:", data1)
    sorted_list = sorter.sort()
    print("Sorted list by age in descending order:", sorted_list)

    data2 = [{'product': 'Laptop', 'price': 1000}, {'product': 'Mouse', 'price': 50}, {'product': 'Keyboard', 'price': 150}]
    sorter = DictSorter(data2, 'price')
    print("\nOriginal list:", data2)
    sorted_list = sorter.sort()
    print("Sorted list by price in descending order:", sorted_list)

    data3 = [{'name': 'David'}, {'name': 'Eve', 'age': 35}, {'name': 'Frank'}]
    sorter = DictSorter(data3, 'age')
    print("\nOriginal list:", data3)
    sorted_list = sorter.sort()
    print("Sorted list by age in descending order (missing key handled gracefully):", sorted_list)

    data4 = []
    sorter = DictSorter(data4, 'any_key')
    print("\nOriginal list:", data4)
    sorted_list = sorter.sort()
    print("Sorted empty list:", sorted_list)