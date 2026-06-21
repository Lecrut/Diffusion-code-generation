def sort_two_floats(a, b):
    return [min(a, b), max(a, b)]

if __name__ == '__main__':
    result = sort_two_floats(3.14, 1.41)
    print(result)