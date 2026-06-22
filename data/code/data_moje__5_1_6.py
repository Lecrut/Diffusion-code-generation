def compare_lengths(a, b):
    if a > b:
        return (a, b, 'greater')
    elif b > a:
        return (b, a, 'less')
    else:
        return (a, b, 'equal')

if __name__ == '__main__':
    result = compare_lengths(5.5, 3.2)
    print(result)
    result2 = compare_lengths(2.1, 7.8)
    print(result2)
    result3 = compare_lengths(4.0, 4.0)
    print(result3)