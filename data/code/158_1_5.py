class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_even_numbers(self):
        return list(range(self.start, self.end + 1))[::2]

if __name__ == '__main__':
    range_instance = NumberRange(1, 10)
    even_numbers = range_instance.get_even_numbers()
    print(even_numbers)