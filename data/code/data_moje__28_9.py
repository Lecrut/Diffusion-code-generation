def sort_floats(a, b):
    if a < b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    result = sort_floats(3.14, 1.59)
    print(result)