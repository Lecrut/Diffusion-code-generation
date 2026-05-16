import collections
class ListSorter:
    def sort_and_display(self, iterable):
        data = list(iterable)
        data.sort()
        print(data)
if __name__ == '__main__':
    sorter = ListSorter()
    sample_list_1 = [5, 2, 8, 1, 9, 4]
    print("Sample 1:")
    sorter.sort_and_display(sample_list_1)
    sample_list_2 = [3, 1, 4, 1, 5, 9, 2, 6]
    print("\nSample 2:")
    sorter.sort_and_display(sample_list_2)
    sample_list_3 = [100, 50, 25, 75, 125]
    print("\nSample 3:")
    sorter.sort_and_display(sample_list_3)
    sample_list_4 = [7, 7, 7, 7]
    print("\nSample 4:")
    sorter.sort_and_display(sample_list_4)