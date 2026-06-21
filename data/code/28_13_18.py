def sort_two_numbers(a, b):
    if a < b:
        return a, b
    return b, a

if __name__ == '__main__':
    first = 15
    second = 42
    result = sort_two_numbers(first, second)
    print(result)