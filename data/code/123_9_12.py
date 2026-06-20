from functools import reduce

def calculate_total(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [3, 6, 9, 12]
    total_sum = calculate_total(sample_values)
    print(total_sum)