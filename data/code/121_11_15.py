def compare_large_integers(a, b):
    max_len = max(len(str(a)), len(str(b)))
    a_str = str(a).zfill(max_len)
    b_str = str(b).zfill(max_len)

    for i in range(max_len):
        if a_str[i] > b_str[i]:
            return 1
        elif a_str[i] < b_str[i]:
            return 0

if __name__ == '__main__':
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    print(compare_large_integers(num1, num2))

    num3 = 123456789
    num4 = 1234567890
    print(compare_large_integers(num3, num4))