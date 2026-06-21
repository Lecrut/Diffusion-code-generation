def sort_two_floats(a, b):
    return (min(a, b), max(a, b))

if __name__ == '__main__':
    x = 3.14
    y = 2.71
    result = sort_two_floats(x, y)
    print(result)