class NumberHandler:
    @staticmethod
    def get_first_last(numbers):
        if numbers:
            return numbers[0], numbers[-1]
        else:
            return None, None

if __name__ == '__main__':
    sample_input = "75 85 95 105"
    numbers = list(map(int, sample_input.split()))
    first_number, last_number = NumberHandler.get_first_last(numbers)
    print(first_number, last_number)