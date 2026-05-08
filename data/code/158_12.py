class NumberProcessor:
    def find_evens(self, numbers):
        evens = []
        for number in numbers:
            if number % 2 == 0:
                evens.append(number)
        return evens
if __name__ == '__main__':
    processor = NumberProcessor()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = processor.find_evens(sample_list)
    print(result)