from functools import reduce

class NumberSummation:
    @staticmethod
    def sum_numbers(numbers):
        return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    total_sum = NumberSummation.sum_numbers(sample_values)
    print(total_sum)