def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_ratio_of_lengths(l1, l2):
    divisor = gcd(l1, l2)
    return (l1 // divisor, l2 // divisor)

if __name__ == '__main__':
    l1 = 48
    l2 = 64
    ratio = find_ratio_of_lengths(l1, l2)
    print(ratio)