class NumericSorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_numbers(self):
        return sorted(map(float, self.numbers))

if __name__ == '__main__':
    sorter = NumericSorter(['3.5', 2, '4', 1.1])
    print(sorter.sort_numbers())