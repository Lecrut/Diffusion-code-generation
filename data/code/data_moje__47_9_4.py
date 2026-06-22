from functools import reduce

def calculate_mean(numbers):
    sum_val = reduce(lambda x, y: x + y, numbers)
    length = reduce(lambda x, y: x + 1, numbers, 0)
    return sum_val / length

if __name__ == '__main__':
    sample_data = [1.5, 2.5, 3.5, 4.5, 5.0]
    result = calculate_mean(sample_data)
    print(result)