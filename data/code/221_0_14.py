class NumberSorter:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]

    def sort(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] > self.numbers[j]:
                    self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]

    def get_sorted_numbers(self):
        return self.numbers

if __name__ == '__main__':
    sorter = NumberSorter(3, 1, 2)
    sorter.sort()
    print(*sorter.get_sorted_numbers())