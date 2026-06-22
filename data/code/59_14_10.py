def digital_root_like_sum(n):
    n = n & ~(1 << 63) if n < 0 else n
    if n == 0:
        return 0
    result = 0
    while n:
        digit = n & 15
        result += digit // 10 + digit % 10 if digit >= 10 else digit
        n >>= 4
    while result >= 10:
        temp = 0
        while result:
            digit = result & 15
            temp += digit // 10 + digit % 10 if digit >= 10 else digit
            result >>= 4
        result = temp
    return result

if __name__ == '__main__':
    print(digital_root_like_sum(0))
    print(digital_root_like_sum(12345))
    print(digital_root_like_sum(-98765))
    print(digital_root_like_sum(99999))
    print(digital_root_like_sum(5))