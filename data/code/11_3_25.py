def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_ratio_of_lengths(l1, l2):
    if l1 == 0 and l2 == 0:
        raise ValueError("Both lengths cannot be zero.")
    common_divisor = gcd(l1, l2)
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor
    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    sample_l1 = 48
    sample_l2 = 60
    ratio = find_ratio_of_lengths(sample_l1, sample_l2)
    print(ratio)