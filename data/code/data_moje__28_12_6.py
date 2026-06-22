def sort_two_floats(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    result = sort_two_floats(3.14, 2.71)
    print(result)