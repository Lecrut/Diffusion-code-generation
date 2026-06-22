class DivisibleNumbers:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end

    def find_divisibles(self):
        return [i for i in range(self.start, self.end + 1) if i % 3 == 0 and i % 5 == 0]

if __name__ == '__main__':
    divisible_numbers = DivisibleNumbers()
    print(divisible_numbers.find_divisibles())