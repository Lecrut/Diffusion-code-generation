def compare_numbers(a: str, b: str) -> bool:
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        return True
    elif len_a < len_b:
        return False
    for i in range(len_a):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    return False
if __name__ == '__main__':
    num1 = '12345678901234567890'
    num2 = '12345678901234567889'
    print(compare_numbers(num1, num2))