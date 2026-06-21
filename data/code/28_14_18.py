def sort_two_numbers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    x = 5
    y = 2
    print(sort_two_numbers(x, y))