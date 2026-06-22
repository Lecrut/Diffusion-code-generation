def sort_two_numbers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    x, y = 5, 3
    result = sort_two_numbers(x, y)
    print(result)