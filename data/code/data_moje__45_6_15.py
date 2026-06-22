from functools import reduce

def find_minimum(values):
    if not values:
        raise ValueError("List must not be empty")
    return reduce(lambda a, b: a if a < b else b, values)

if __name__ == '__main__':
    numbers = [10, 4, 7, 1, 9, 15, 3]
    result = find_minimum(numbers)
    print(result)