class NumberFilter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_divisible_by_3_and_5(self):
        for number in range(self.start, self.end + 1):
            if number % 3 == 0 and number % 5 == 0:
                yield number

if __name__ == '__main__':
    filter_instance = NumberFilter(1, 100)
    divisible_numbers = list(filter_instance.get_divisible_by_3_and_5())
    for number in divisible_numbers:
        print(number)