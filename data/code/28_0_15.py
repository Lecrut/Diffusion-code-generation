def sort_two_numbers(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_two_numbers(5, 3))
    print(sort_two_numbers(10, 10))
    print(sort_two_numbers(-1, 4))