from functools import reduce

def calculate_mean(values):
    total = reduce(lambda x, y: x + y, values)
    count = len(values)
    return total / count if count > 0 else 0.0

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5, 5.5]
    result = calculate_mean(sample_values)
    print(result)