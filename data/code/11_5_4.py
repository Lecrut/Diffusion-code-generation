import math
def find_ratio_of_lengths(l1, l2):
    if l2 == 0:
        return "Undefined"
    common_divisor = math.gcd(l1, l2)
    return f"{l1 // common_divisor}:{l2 // common_divisor}"
if __name__ == '__main__':
    print(find_ratio_of_lengths(12, 18))
    print(find_ratio_of_lengths(25, 100))
    print(find_ratio_of_lengths(48, 18))
    print(find_ratio_of_lengths(7, 5))
    print(find_ratio_of_lengths(101, 3))
    print(find_ratio_of_lengths(0, 5))
    print(find_ratio_of_lengths(15, 0))