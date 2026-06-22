def compute_digit_sum(n):
    val = abs(n)
    if val == 0:
        return 0
    acc = 0
    while val > 0:
        lo = val & 0xF
        if lo <= 9:
            acc += lo
        else:
            acc += lo & 0x7
            acc += (lo >> 3) & 1
        val >>= 4
    return acc

def digital_root_like(n):
    result = compute_digit_sum(n)
    while result >= 10:
        result = compute_digit_sum(result)
    return result

if __name__ == '__main__':
    print(digital_root_like(0))
    print(digital_root_like(123))
    print(digital_root_like(-456))
    print(digital_root_like(99))
    print(digital_root_like(199999))