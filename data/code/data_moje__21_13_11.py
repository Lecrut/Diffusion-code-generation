def find_highest_value(a, b, c):
    highest = a
    if b > highest:
        highest = b
    if c > highest:
        highest = c
    return highest

if __name__ == '__main__':
    val1 = 10.5
    val2 = 25.3
    val3 = 15.7
    result = find_highest_value(val1, val2, val3)
    print(result)