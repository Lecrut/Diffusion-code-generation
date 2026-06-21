import builtins

def find_largest(a, b, c):
    return builtins.max(a, b, c)

if __name__ == '__main__':
    x = 10
    y = 25
    z = 7
    result = find_largest(x, y, z)
    print(result)