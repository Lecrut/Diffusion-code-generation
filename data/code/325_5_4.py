def compare_numbers(str1, str2):
    num1 = int(str1)
    num2 = int(str2)
    if num1 > num2:
        return str1
    elif num2 > num1:
        return str2
    else:
        return str1
if __name__ == '__main__':
    a = '10'
    b = '5'
    result1 = compare_numbers(a, b)
    print(result1)
    c = '25'
    d = '15'
    result2 = compare_numbers(c, d)
    print(result2)
    e = '7'
    f = '99'
    result3 = compare_numbers(e, f)
    print(result3)
    g = '42'
    h = '42'
    result4 = compare_numbers(g, h)
    print(result4)