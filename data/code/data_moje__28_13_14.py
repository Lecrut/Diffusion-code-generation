def sort_two_numbers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    print(sort_two_numbers(5, 3))
    print(sort_two_numbers(1, 100))
    print(sort_two_numbers(-5, 5))
    print(sort_two_numbers(0, 0))