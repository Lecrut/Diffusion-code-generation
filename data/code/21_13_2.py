from functools import cmp_to_key
class Sorter:
    def sort_data(self, data_list, key_function):
        def compare(a, b):
            if key_function(a) < key_function(b):
                return -1
            elif key_function(a) > key_function(b):
                return 1
            else:
                return 0
        return sorted(data_list, key=cmp_to_key(compare))
if __name__ == '__main__':
    sorter = Sorter()
    data1 = [('apple', 5), ('banana', 2), ('cherry', 8)]
    def key1(item):
        return item[1]
    sorted_data1 = sorter.sort_data(data1, key1)
    print("Sorted Data 1:")
    print(sorted_data1)
    data2 = [('a', 3), ('b', 1), ('c', 2)]
    def key2(item):
        return ord(item[0])
    sorted_data2 = sorter.sort_data(data2, key2)
    print("\nSorted Data 2:")
    print(sorted_data2)
    data3 = [(1, 'z'), (3, 'a'), (2, 'm')]
    def key3(item):
        return item[1]
    sorted_data3 = sorter.sort_data(data3, key3)
    print("\nSorted Data 3:")
    print(sorted_data3)