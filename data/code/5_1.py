def compare_lengths(a, b):
    if a > b:
        return ('greater', a, b)
    elif a < b:
        return ('less', a, b)
    else:
        return ('equal', a, b)

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    result = compare_lengths(val1, val2)
    print(result)