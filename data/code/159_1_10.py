class NumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_odd(self):
        return [x for x in self.numbers if x % 2 != 0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_instance = NumberFilter(sample_list)
    odd_numbers = filter_instance.filter_odd()
    print(odd_numbers)