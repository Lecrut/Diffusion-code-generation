class NumberProcessor:
    def filter_odd_numbers(self, numbers: list) -> list:
        odd_numbers = []
        for number in numbers:
            if number % 2 != 0:
                odd_numbers.append(number)
        return odd_numbers
if __name__ == '__main__':
    processor = NumberProcessor()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = processor.filter_odd_numbers(sample_list)
    print(result)