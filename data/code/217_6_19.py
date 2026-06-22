def compare_large_integers(a: str, b: str) -> int:
    len_a = len(a)
    len_b = len(b)

    if len_a > len_b:
        return 1
    elif len_a < len_b:
        return -1

    for i in range(len_a):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1

    return 0

if __name__ == '__main__':
    result = compare_large_integers('12345678901234567890', '98765432109876543210')
    print(result)