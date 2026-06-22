class NumberSorter:
    def __init__(self, numbers):
        self.numbers = sorted(numbers)

    def get_sorted_numbers(self):
        return self.numbers

if __name__ == '__main__':
    sorter = NumberSorter([15, 7, 22])
    print(*sorter.get_sorted_numbers())