def sort_two_floats(a, b):
    return (min(a, b), max(a, b))

if __name__ == '__main__':
    a = 3.14
    b = 2.71
    result = sort_two_floats(a, b)
    print(result)