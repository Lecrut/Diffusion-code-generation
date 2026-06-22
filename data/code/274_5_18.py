class NumberSorter:
    @staticmethod
    def sort_and_print(numbers):
        numbers.sort()
        for number in numbers:
            print(number)

if __name__ == '__main__':
    sorter = NumberSorter()
    sample_list = [10, 25, 33, 47, 51]
    sorter.sort_and_print(sample_list)