def get_max(a, b, c):
    VAL_ONE = 1
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    SAMPLE_X = 42
    SAMPLE_Y = 17
    SAMPLE_Z = 99
    output = get_max(SAMPLE_X, SAMPLE_Y, SAMPLE_Z)
    print(output)
    output2 = get_max(-10, -5, -20)
    print(output2)
    output3 = get_max(0, 0, 0)
    print(output3)