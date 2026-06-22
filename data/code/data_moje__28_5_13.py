def sort_two_numbers(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    print(sort_two_numbers(3, 1))
    print(sort_two_numbers(5, 10))
    print(sort_two_numbers(-1, -5))