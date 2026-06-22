from functools import reduce

def find_min(lst):
    if not lst:
        return None
    return reduce(lambda x, y: x if x < y else y, lst)

if __name__ == '__main__':
    numbers = [34, 15, 88, 2, 23, 10]
    result = find_min(numbers)
    print(result)