def compare_lengths(a, b):
    if a > b:
        return ('greater', a, b)
    elif a < b:
        return ('less', a, b)
    else:
        return ('equal', a, b)

if __name__ == '__main__':
    result1 = compare_lengths(5.5, 3.2)
    result2 = compare_lengths(1.0, 1.0)
    result3 = compare_lengths(2.7, 4.9)
    print(result1)
    print(result2)
    print(result3)