def compare_lengths(a, b):
    if a > b:
        return ('greater', a - b)
    elif a < b:
        return ('less', b - a)
    else:
        return ('equal', 0.0)

if __name__ == '__main__':
    result1 = compare_lengths(5.0, 3.0)
    print(result1)
    result2 = compare_lengths(2.5, 7.5)
    print(result2)
    result3 = compare_lengths(4.0, 4.0)
    print(result3)