def find_largest(x, y, z):
    result = max(x, y, z)
    return result

if __name__ == '__main__':
    val1 = 100
    val2 = 200
    val3 = 150
    output = find_largest(val1, val2, val3)
    print(output)