def sort_two_numbers(a, b):
    if a <= b:
        return a, b
    return b, a

if __name__ == '__main__':
    x, y = sort_two_numbers(10, 2)
    print(x, y)