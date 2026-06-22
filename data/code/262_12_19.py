class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_min_max(self):
        if not self.numbers:
            return None, None
        smallest = largest = self.numbers[0]
        for number in self.numbers[1:]:
            if number < smallest:
                smallest = number
            elif number > largest:
                largest = number
        return smallest, largest

if __name__ == '__main__':
    finder = MinMaxFinder([15, -3, 88, -42, 99, 1])
    smallest, largest = finder.find_min_max()
    print(f"Input sequence: [15, -3, 88, -42, 99, 1]")
    print(f"Smallest value: {smallest}")
    print(f"Largest value: {largest}")