class NumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_even(self, num):
        return num % 2 == 0

    def is_greater_than_five(self, num):
        return num > 5

    def combine_conditions(self):
        result = []
        for num in self.numbers:
            if self.is_even(num) and self.is_greater_than_five(num):
                result.append(num)
        return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_instance = NumberFilter(data)
    filtered_numbers = filter_instance.combine_conditions()
    print(filtered_numbers)