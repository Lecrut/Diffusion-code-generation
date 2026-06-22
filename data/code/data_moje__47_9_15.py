from functools import reduce

def calculate_mean(values):
    total = reduce(lambda x, y: x + y, values)
    count = reduce(lambda x, _: x + 1, values, 0)
    return total / count

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 15.7, 25.0, 8.5]
    result = calculate_mean(sample_values)
    print(result)