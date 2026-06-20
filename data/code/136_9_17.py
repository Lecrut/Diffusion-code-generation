class NumberFilter:
    def __init__(self):
        self.sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def filter_transform(self):
        return (x * 2 for x in self.sample_numbers if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    number_filter = NumberFilter()
    result = number_filter.filter_transform()
    print(list(result))