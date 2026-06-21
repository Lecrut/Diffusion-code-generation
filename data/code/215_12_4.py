def find_max(iterable):
    if not iterable:
        return None
    max_value = float('-inf')
    for value in iterable:
        if value > max_value:
            max_value = value
    return max_value
if __name__ == '__main__':
    print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
    print(find_max([]))
    print(find_max([-1, -2, -3, -4, -5]))