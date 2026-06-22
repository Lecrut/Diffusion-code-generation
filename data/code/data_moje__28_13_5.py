def sort_two_numbers(a, b):
    if a <= b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    result = sort_two_numbers(5, 2)
    print(result)
    result = sort_two_numbers(-10, 100)
    print(result)
    result = sort_two_numbers(0, 0)
    print(result)