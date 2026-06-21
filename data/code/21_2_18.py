def find_largest(a, b, c):
    max_ab = a if a > b else b
    return max_ab if max_ab > c else c

if __name__ == '__main__':
    result = find_largest(10, 25, 15)
    print(result)