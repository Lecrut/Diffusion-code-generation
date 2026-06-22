def sort_two_numbers(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    print(sort_two_numbers(5, 3))
    print(sort_two_numbers(1, 1))
    print(sort_two_numbers(-2, 4))