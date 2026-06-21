def sort_two_floats(a, b):
    if a < b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    x = 5.7
    y = 2.3
    result = sort_two_floats(x, y)
    print(result)