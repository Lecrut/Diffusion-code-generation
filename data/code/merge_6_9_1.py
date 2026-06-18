import math
def product_of_list(numbers):
    return math.prod(numbers)
if __name__ == '__main__':
    data = [2, 3, 5, 10]
    result = product_of_list(data)
    print(result)