class ListSorter:
    @staticmethod
    def sort_ascending(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    print(ListSorter.sort_ascending(sample_values))
    print(ListSorter.sort_ascending([]))
    print(ListSorter.sort_ascending([1, 1, 1, 1]))