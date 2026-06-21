class ListSorter:
    @staticmethod
    def sort_large_list(items):
        return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 2, 9, 1, 7, 4]
    sorter = ListSorter()
    sorted_values = sorter.sort_large_list(sample_values)
    print(sorted_values)