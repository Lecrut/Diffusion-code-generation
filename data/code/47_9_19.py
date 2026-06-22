from functools import reduce

def calculate_mean(numbers):
    return reduce(lambda acc, x: acc + x, map(float, numbers)) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.1, 5.9]
    result = calculate_mean(sample_values)
    print(result)