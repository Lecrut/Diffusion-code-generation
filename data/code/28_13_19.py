def sort_two_numbers(a, b):
    if a < b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    first = 42
    second = 15
    result = sort_two_numbers(first, second)
    print(result)