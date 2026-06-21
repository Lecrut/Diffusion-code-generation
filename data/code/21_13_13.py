def find_highest(a, b, c):
    highest = a
    if b > highest:
        highest = b
    if c > highest:
        highest = c
    return highest

if __name__ == '__main__':
    val1 = 15.5
    val2 = 23.7
    val3 = 8.2
    result = find_highest(val1, val2, val3)
    print(result)