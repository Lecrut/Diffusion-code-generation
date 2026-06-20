def compare_lengths(a, b):
    if a > b:
        return ("a", "greater")
    elif a < b:
        return ("b", "greater")
    else:
        return ("equal", None)

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    result = compare_lengths(val1, val2)
    print(result)
    val3 = 3.14
    val4 = 3.14
    result2 = compare_lengths(val3, val4)
    print(result2)
    val5 = 1.0
    val6 = 5.0
    result3 = compare_lengths(val5, val6)
    print(result3)