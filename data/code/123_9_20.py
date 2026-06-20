from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [12, 14, 16, 18]
    total_sum = sum_numbers(sample_values)
    print(total_sum)