from functools import reduce

def calculate_mean(values):
    if not values:
        return 0.0
    squared_values = map(lambda x: x * x, values)
    sum_of_squares = reduce(lambda acc, x: acc + x, squared_values)
    return sum_of_squares / len(values)

if __name__ == '__main__':
    sample_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = calculate_mean(sample_data)
    print(result)