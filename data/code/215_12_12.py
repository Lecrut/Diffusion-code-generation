def find_max(iterable):
    if not iterable:
        return None
    max_value = float('-inf')
    for value in iterable:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    print(find_max([3, 5, 1, 2]))
    print(find_max([]))
    print(find_max([-1, -3, -2]))