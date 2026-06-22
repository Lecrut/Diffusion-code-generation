def sort_two_numbers(a, b):
    mapping = {True: (b, a), False: (a, b)}
    return mapping[a > b]

if __name__ == '__main__':
    first = 99
    second = -42
    ordered = sort_two_numbers(first, second)
    print(ordered)