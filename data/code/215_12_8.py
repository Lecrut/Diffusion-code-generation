def find_max(iterable):
    if not iterable:
        return None
    maximum = iterable[0]
    for number in iterable:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    print(find_max([3, 5, 1, 2]))
    print(find_max([]))
    print(find_max([-1, -3, -2]))