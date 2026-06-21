class StringSorter:
    def sort_strings(self, arr):
        return sorted(arr, key=int)

if __name__ == '__main__':
    sorter = StringSorter()
    string_list = ["34", "12", "98765", "234"]
    print("Original list:", string_list)
    sorted_list = sorter.sort_strings(string_list)
    print("Sorted list:", sorted_list)