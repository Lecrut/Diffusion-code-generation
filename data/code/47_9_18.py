from functools import reduce

def calculate_mean(values):
    total = reduce(lambda a, b: a + b, values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    numbers = [1.5, 2.5, 3.5, 4.5]
    mean_value = calculate_mean(numbers)
    print(mean_value)