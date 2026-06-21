def get_highest_value(val1, val2, val3):
    highest = val1
    if val2 > highest:
        highest = val2
    if val3 > highest:
        highest = val3
    return highest

if __name__ == '__main__':
    a = 10.5
    b = 20.3
    c = 15.0
    result = get_highest_value(a, b, c)
    print(result)