def sort_two_floats(a, b):
    minimum = min(a, b)
    maximum = max(a, b)
    return (minimum, maximum)

if __name__ == '__main__':
    result = sort_two_floats(3.14, 2.71)
    print(result)