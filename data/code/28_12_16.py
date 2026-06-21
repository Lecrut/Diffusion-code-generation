def sort_two_floats(a, b):
    if a < b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    result = sort_two_floats(5.5, 2.2)
    print(result)