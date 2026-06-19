def find_ratio_of_lengths(l1, l2):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if l2 == 0:
        raise ValueError("l2 must not be zero")

    common_divisor = gcd(l1, l2)
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor

    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    l1 = 48
    l2 = 180
    print(find_ratio_of_lengths(l1, l2))