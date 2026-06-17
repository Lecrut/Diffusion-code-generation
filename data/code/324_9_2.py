import functools
def calculate_product(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)
if __name__ == '__main__':
    data = [2, 3, 5, 7]
    result = calculate_product(data)
    print(result)