import functools
def calculate_product(numbers):
    if not numbers:
        return 1
    return functools.reduce(lambda x, y: x * y, numbers)
if __name__ == '__main__':
    data = [2, 3, 4, 5]
    result = calculate_product(data)
    print(result)