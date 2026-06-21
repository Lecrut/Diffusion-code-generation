class NumberProcessor:
    def __init__(self):
        self.odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15}

    def find_even_numbers(self):
        all_numbers = set(range(1, 16))
        return all_numbers - self.odd_numbers

if __name__ == '__main__':
    processor = NumberProcessor()
    even_numbers = processor.find_even_numbers()
    print(even_numbers)