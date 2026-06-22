def digital_root_like_sum(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    while n >= 10:
        total = 0
        temp = n
        while temp > 0:
            total += temp & 15
            temp >>= 4
        n = total
    return n

if __name__ == '__main__':
    print(digital_root_like_sum(0))
    print(digital_root_like_sum(12345))
    print(digital_root_like_sum(-9876))
    print(digital_root_like_sum(99))
    print(digital_root_like_sum(10))