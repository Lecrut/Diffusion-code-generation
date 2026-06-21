class ListSorter:
    @staticmethod
    def sort_large_list(items):
        return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [15, 23, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorter = ListSorter()
    print(sorter.sort_large_list(sample_values))