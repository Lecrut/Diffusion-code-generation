import collections
class ListSorter:
    def sort_and_display(self, iterable):
        data = list(iterable)
        data.sort()
        print("Sorted List:")
        for item in data:
            print(item)
if __name__ == '__main__':
    sorter = ListSorter()
    sample_data_1 = [5, 2, 8, 1, 9, 4, 3, 7, 6]
    print("--- Sample 1 ---")
    sorter.sort_and_display(sample_data_1)
    sample_data_2 = [100, 50, 25, 75, 125]
    print("\n--- Sample 2 ---")
    sorter.sort_and_display(sample_data_2)
    sample_data_3 = [3.14, 1.618, 2.718, 0.577]
    print("\n--- Sample 3 ---")
    sorter.sort_and_display(sample_data_3)