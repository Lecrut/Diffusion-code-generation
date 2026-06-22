class NumberHandler:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_difference(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_numbers = (3.5, 7.8, 1.2, 9.4)
    handler = NumberHandler(sample_numbers)
    difference = handler.calculate_difference()
    print(difference)