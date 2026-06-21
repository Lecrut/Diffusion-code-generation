class NumberProcessor:
    def __init__(self):
        self.numbers = [3, 5, 8, 10, 23, 45, 60, 70]

    def process_numbers(self):
        for number in self.numbers:
            if number > 50:
                break
            if number % 2 == 0:
                continue
            print(number)

if __name__ == '__main__':
    processor = NumberProcessor()
    processor.process_numbers()