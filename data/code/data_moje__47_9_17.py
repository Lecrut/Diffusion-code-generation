from functools import reduce

def calculate_mean(values):
    return reduce(lambda x, y: x + y, map(lambda x: float(x), values)) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.1, 5.9]
    result = calculate_mean(sample_values)
    print(result)