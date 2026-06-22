class MinFinder:
    def __init__(self):
        self.numbers = []

    def add_numbers(self, numbers):
        self.numbers.extend(numbers)

    def get_minimum(self):
        if not self.numbers:
            return None
        minimum = self.numbers[0]
        for number in self.numbers[1:]:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    mf = MinFinder()
    sample_data1 = [5, 2, 8, 1, 9]
    mf.add_numbers(sample_data1)
    print(f"Minimum of {sample_data1}: {mf.get_minimum()}")

    sample_data2 = [10, -4, 22, 8, 15]
    mf.add_numbers(sample_data2)
    print(f"Updated minimum after adding {sample_data2}: {mf.get_minimum()}")