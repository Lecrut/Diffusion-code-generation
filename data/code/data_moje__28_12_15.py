def sort_two_floats(a, b):
    if a > b:
        return [b, a]
    return [a, b]

if __name__ == '__main__':
    print(sort_two_floats(3.14, 2.71))