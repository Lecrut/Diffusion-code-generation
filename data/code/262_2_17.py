MAX_INITIAL_CAPACITY = 10

class MinMaxFinder:
    def __init__(self):
        self.numbers = [None] * MAX_INITIAL_CAPACITY
        self.count = 0

    def add_number(self, number):
        if self.count >= len(self.numbers):
            self._resize()
        self.numbers[self.count] = number
        self.count += 1

    def _resize(self):
        new_capacity = len(self.numbers) * 2
        new_numbers = [None] * new_capacity
        for i in range(self.count):
            new_numbers[i] = self.numbers[i]
        self.numbers = new_numbers

    def find_min_max(self):
        if self.count == 0:
            return None, None
        minimum = maximum = self.numbers[0]
        for number in self.numbers[:self.count]:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return minimum, maximum

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data1 = [10, 5, 20, 3, 15]
    for num in sample_data1:
        finder.add_number(num)
    min1, max1 = finder.find_min_max()
    print(f"Data set 1: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")