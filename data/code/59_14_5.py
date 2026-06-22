def digital_root_sum(n):
    n = abs(n)
    while n >= 10:
        total = 0
        while n > 0:
            total += n & 0xF
            total += (n >> 4) & 0xF
            total += (n >> 8) & 0xF
            total += (n >> 12) & 0xF
            total += (n >> 16) & 0xF
            total += (n >> 20) & 0xF
            total += (n >> 24) & 0xF
            total += (n >> 28) & 0xF
            total += (n >> 32) & 0xF
            total += (n >> 36) & 0xF
            total += (n >> 40) & 0xF
            total += (n >> 44) & 0xF
            total += (n >> 48) & 0xF
            total += (n >> 52) & 0xF
            total += (n >> 56) & 0xF
            n = total
            if n < 10:
                break
            n = 0
            temp = total
            while temp > 0:
                n += temp % 10
                temp //= 10
            total = n
        n = total
    return n

if __name__ == '__main__':
    print(digital_root_sum(0))
    print(digital_root_sum(-9999))
    print(digital_root_sum(12345))
    print(digital_root_sum(99))
    print(digital_root_sum(10))