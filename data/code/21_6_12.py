def find_greatest(a, b, c):
    return a if (a >= b and a >= c) else (b if b >= c else c)

if __name__ == '__main__':
    result = find_greatest(10, 25, 15)
    print(result)