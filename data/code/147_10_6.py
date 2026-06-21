class Sorter:
    def timsort_ascending(self, numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sorter = Sorter()
    sample_values = [34, 7, 23, 32, 5, 62]
    empty_list = []
    duplicate_values = [1, 1, 1, 1]

    print(sorter.timsort_ascending(sample_values))
    print(sorter.timsort_ascending(empty_list))
    print(sorter.timsort_ascending(duplicate_values))