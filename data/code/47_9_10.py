from functools import reduce

def calculate_mean(numbers):
    if not numbers:
        return 0
    squared_values = list(map(lambda x: x * x, numbers))
    sum_of_squares = reduce(lambda a, b: a + b, squared_values)
    count = len(numbers)
    mean_of_squares = sum_of_squares / count
    return mean_of_squares

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = calculate_mean(sample_values)
    print(result)