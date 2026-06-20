class ListSortChecker:
    @staticmethod
    def is_sorted_ascending(lst):
        if not lst:
            return True
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = ListSortChecker.is_sorted_ascending(sample_list)
    print(result)