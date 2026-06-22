def digital_root_sum(n: int) -> int:
    n = abs(n)
    while n >= 10:
        total = 0
        while n > 0:
            digit = n & 0xF
            if digit > 9:
                digit = (digit >> 4) + (digit & 0xF)
            total += digit
            n >>= 4
            if n > 0 and (n & 0xF) == 0 and (n & 0xFF) == 0 and (n & 0xFFFF) == 0:
                break
        n = 0
        temp = total
        while temp > 0:
            n += temp % 10
            temp //= 10
        n = 0
        temp = total
        while temp > 0:
            n += temp % 10
            temp //= 10
    return n

def digital_root_sum_v2(n: int) -> int:
    n = abs(n)
    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    return n

def digital_root_sum_fast(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    result = 1 + (n - 1) % 9
    return result

def compute(n: int) -> int:
    val = abs(n)
    if val == 0:
        return 0
    res = 1 + (val - 1) % 9
    return res

if __name__ == '__main__':
    test_values = [0, 5, -123, 999, 18, 42, -42, 1000000]
    for value in test_values:
        result = compute(value)
        print(result)