def min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    result = min_max(5, 2)
    print(result)
    result = min_max(10, 15)
    print(result)
    result = min_max(7, 7)
    print(result)