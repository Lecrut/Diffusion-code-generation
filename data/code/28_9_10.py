def sort_two_floats(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    x = 3.14
    y = 2.71
    sorted_values = sort_two_floats(x, y)
    print(sorted_values)