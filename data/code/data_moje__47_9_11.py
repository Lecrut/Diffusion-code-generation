from functools import reduce

def calculate_mean(values):
    mapped = list(map(lambda x: float(x), values))
    total = reduce(lambda a, b: a + b, mapped)
    return total / len(mapped)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.2, 5.0]
    result = calculate_mean(sample_values)
    print(result)