def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_ratio_of_lengths(l1, l2):
    if l1 == 0 or l2 == 0:
        return None
    common_divisor = gcd(l1, l2)
    return (l1 // common_divisor, l2 // common_divisor)

if __name__ == '__main__':
    sample_l1 = 48
    sample_l2 = 36
    ratio = find_ratio_of_lengths(sample_l1, sample_l2)
    print(ratio)