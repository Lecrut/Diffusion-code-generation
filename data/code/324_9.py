import functools
def product_of_list(numbers):
    if not numbers:
        return 1
    return functools.reduce(lambda x, y: x * y, numbers)
if __name__ == '__main__':
    data = [2, 3, 5, 7]
    result = product_of_list(data)
    print(result)