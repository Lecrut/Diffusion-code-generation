from functools import reduce
def calculate_sum(sequence):
    return reduce(lambda acc, x: acc + x, sequence)
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(result)