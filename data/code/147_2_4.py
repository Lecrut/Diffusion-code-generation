import collections
class ListSorter:
    def sort_and_display(self, iterable):
        data = list(iterable)
        data.sort()
        print(data)
if __name__ == '__main__':
    sorter = ListSorter()
    sample1 = [5, 2, 8, 1, 9, 4]
    print("Sample 1:")
    sorter.sort_and_display(sample1)
    sample2 = [3.14, 1.618, 2.718, 0.577]
    print("\nSample 2:")
    sorter.sort_and_display(sample2)
    sample3 = ["banana", "apple", "cherry", "date"]
    print("\nSample 3:")
    sorter.sort_and_display(sample3)
    sample4 = [100, -5, 0, 50, -100]
    print("\nSample 4:")
    sorter.sort_and_display(sample4)