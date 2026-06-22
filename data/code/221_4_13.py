class NumberSorter:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]

    def sort_numbers(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] > self.numbers[j]:
                    self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]
        return self.numbers

if __name__ == '__main__':
    sorter = NumberSorter(3.14, 2.71, 1.61)
    sorted_numbers = sorter.sort_numbers()
    print(*sorted_numbers)