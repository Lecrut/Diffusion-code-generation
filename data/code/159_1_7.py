class NumberFilter:
    def filter_odd(self, numbers):
        return [x for x in numbers if x % 2 != 0]

if __name__ == '__main__':
    filter_instance = NumberFilter()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_instance.filter_odd(sample_list)
    print(result)