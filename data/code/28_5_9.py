def sort_two_numbers(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    print(sort_two_numbers(5, 2))
    print(sort_two_numbers(10, 30))
    print(sort_two_numbers(7, 7))