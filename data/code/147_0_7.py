class Sorter:
    @staticmethod
    def sort_ascending(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    sorter = Sorter()
    sorted_list = sorter.sort_ascending(sample_list)
    print(sorted_list)