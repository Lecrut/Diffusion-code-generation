class NumberProcessor:
    def find_evens(self, numbers):
        for number in numbers:
            if number % 2 == 0:
                yield number
if __name__ == '__main__':
    processor = NumberProcessor()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_generator = processor.find_evens(sample_list)
    even_list = list(even_generator)
    print(even_list)