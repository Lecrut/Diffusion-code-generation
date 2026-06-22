from functools import reduce

def mean_of_list(numbers):
    def add(x, y):
        return x + y
    total = reduce(add, numbers)
    count = len(numbers)
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_values = [10.5, 20.0, 30.5, 40.0, 50.0]
    result = mean_of_list(sample_values)
    print(result)