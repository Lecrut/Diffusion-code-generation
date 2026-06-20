def compare_lengths(a, b):
    if a > b:
        return ('greater', a, b)
    if a < b:
        return ('less', a, b)
    return ('equal', a, b)

if __name__ == '__main__':
    val1 = 10.5
    val2 = 10.2
    result = compare_lengths(val1, val2)
    print(result)
    val3 = 10.2
    val4 = 10.5
    result2 = compare_lengths(val3, val4)
    print(result2)
    val5 = 7.0
    val6 = 7.0
    result3 = compare_lengths(val5, val6)
    print(result3)