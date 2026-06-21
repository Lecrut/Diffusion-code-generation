class NumberFilter:
    def filter_evens(self, numbers):
        return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    processor = NumberFilter()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = processor.filter_evens(sample_list)
    print(result)