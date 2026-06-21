def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_ratio_of_lengths(l1, l2):
    if l1 == 0 or l2 == 0:
        raise ValueError("Lengths must be non-zero")
    
    common_divisor = gcd(l1, l2)
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor
    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    lengths = {
        'l1': 72,
        'l2': 96
    }
    
    ratio = find_ratio_of_lengths(lengths['l1'], lengths['l2'])
    print(ratio)