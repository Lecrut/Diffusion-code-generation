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
    x = '25'
    y = '30'
    result2 = compare_numbers(x, y)
    print(result2)
    p = '100'
    q = '100'
    result3 = compare_numbers(p, q)
    print(result3)