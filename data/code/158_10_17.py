class NumberProcessor:
    def __init__(self, start=0, end=50):
        self.start = start
        self.end = end

    def get_even_numbers(self):
        return [num for num in range(self.start, self.end + 1) if num % 2 == 0]

if __name__ == '__main__':
    processor = NumberProcessor()
    even_numbers = processor.get_even_numbers()
    print(even_numbers)