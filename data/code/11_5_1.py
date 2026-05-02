import math
def find_ratio_of_lengths(l1, l2):
    if l2 == 0:
        return "Undefined"
    common_divisor = math.gcd(l1, l2)
    ratio_l1 = l1 // common_divisor
    ratio_l2 = l2 // common_divisor
    return f"{ratio_l1}:{ratio_l2}"
if __name__ == '__main__':
    print(find_ratio_of_lengths(12, 18))
    print(find_ratio_of_lengths(100, 75))
    print(find_ratio_of_lengths(48, 18))
    print(find_ratio_of_lengths(7, 13))
    print(find_ratio_of_lengths(0, 5))
    print(find_ratio_of_lengths(20, 0))