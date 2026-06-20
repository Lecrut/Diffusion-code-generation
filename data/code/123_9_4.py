from functools import reduce

def total_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = total_sum(sample_values)
    print(result)