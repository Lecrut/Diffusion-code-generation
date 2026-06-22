class RangeProcessor:
    def filter_even_numbers(self, start, end):
        return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    processor = RangeProcessor()
    result = processor.filter_even_numbers(100, 200)
    print(result)