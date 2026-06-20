class NumberHandler:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_first_last(self):
        if self.numbers:
            return self.numbers[0], self.numbers[-1]
        else:
            return None, None

if __name__ == '__main__':
    sample_input = "25 35 45 55"
    numbers = list(map(int, sample_input.split()))
    handler = NumberHandler(numbers)
    first_number, last_number = handler.get_first_last()
    print(first_number, last_number)