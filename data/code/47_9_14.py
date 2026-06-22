from functools import reduce

def calculate_mean(values):
    return reduce(lambda x, y: x + y, map(float, values)) / len(values)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.7, 40.2, 50.1]
    result = calculate_mean(sample_values)
    print(result)