class Sorter:
    DEFAULT_SAMPLE = [10, 4, 6, 8, 2, 9, 5]

    @staticmethod
    def sort_ascending(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sorter_instance = Sorter()
    sample_list = Sorter.DEFAULT_SAMPLE
    sorted_list = sorter_instance.sort_ascending(sample_list)
    print(sorted_list)