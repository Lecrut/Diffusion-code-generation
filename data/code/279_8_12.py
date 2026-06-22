class NumberSquarer:
    def __init__(self, numbers):
        self.numbers = numbers

    def square_numbers(self):
        return [num ** 2 for num in self.numbers]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    squarer = NumberSquarer(sample_values)
    squared_values = squarer.square_numbers()
    print(squared_values)