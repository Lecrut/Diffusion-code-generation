def sort_two_numbers(a, b):
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    x = 15
    y = 7
    result = sort_two_numbers(x, y)
    print(result)