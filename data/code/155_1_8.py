from functools import reduce

def calculate_total():
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    return total

if __name__ == '__main__':
    result = calculate_total()
    print(result)