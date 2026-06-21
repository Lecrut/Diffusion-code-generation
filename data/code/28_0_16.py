def sort_two_numbers(a, b):
    return tuple(sorted([a, b]))

if __name__ == '__main__':
    print(sort_two_numbers(5, 2))
    print(sort_two_numbers(10, 10))
    print(sort_two_numbers(-3, 7))
    print(sort_two_numbers(0, -1))