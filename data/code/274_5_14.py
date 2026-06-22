class NumberSorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_and_print(self):
        sorted_numbers = sorted(self.numbers)
        for number in sorted_numbers:
            print(number)

if __name__ == '__main__':
    sorter = NumberSorter([10, 25, 33, 47, 51])
    sorter.sort_and_print()