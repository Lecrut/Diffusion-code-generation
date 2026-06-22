def min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    result = min_max(5, 3)
    print(result)