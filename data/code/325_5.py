def compare_numbers(str1, str2):
    num1 = int(str1)
    num2 = int(str2)
    if num1 > num2:
        return str1
    else:
        return str2
if __name__ == '__main__':
    a = '10'
    b = '5'
    result1 = compare_numbers(a, b)
    print(f"Comparing {a} and {b}, the larger is: {result1}")
    c = '25'
    d = '15'
    result2 = compare_numbers(c, d)
    print(f"Comparing {c} and {d}, the larger is: {result2}")
    e = '7'
    f = '7'
    result3 = compare_numbers(e, f)
    print(f"Comparing {e} and {f}, the larger is: {result3}")