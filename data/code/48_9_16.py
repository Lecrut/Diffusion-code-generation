from functools import reduce

def get_max(values):
    return reduce(lambda a, b: a if a > b else b, values)

if __name__ == '__main__':
    print(get_max([1, 5, 3, 9, 2, 7]))