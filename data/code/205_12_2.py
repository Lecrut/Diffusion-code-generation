class Sorter:
    def sort_list(self, data):
        data.sort()
if __name__ == '__main__':
    sorter = Sorter()
    sample_list = [5, 2, 8, 1, 9, 4]
    print("Original list:", sample_list)
    sorter.sort_list(sample_list)
    print("Sorted list:", sample_list)
    sample_list_2 = [3, 1, 4, 1, 5, 9, 2, 6]
    print("\nOriginal list:", sample_list_2)
    sorter.sort_list(sample_list_2)
    print("Sorted list:", sample_list_2)