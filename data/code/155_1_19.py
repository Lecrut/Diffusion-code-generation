from functools import reduce

def compute_total():
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    return total

if __name__ == '__main__':
    result = compute_total()
    print(result)