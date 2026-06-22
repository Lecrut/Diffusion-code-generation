def sort_floats(a, b):
    if a > b:
        return [b, a]
    return [a, b]

if __name__ == '__main__':
    result = sort_floats(3.14, 1.59)
    print(result)