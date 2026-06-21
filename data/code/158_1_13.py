class NumberRangeProcessor:
    @staticmethod
    def get_even_numbers(start, end):
        return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    even_numbers = NumberRangeProcessor.get_even_numbers(1, 10)
    print(even_numbers)