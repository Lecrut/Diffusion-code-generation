import math
def find_ratio_of_lengths(l1, l2):
    if l2 == 0:
        return "Undefined"
    common_divisor = math.gcd(l1, l2)
    return (l1 // common_divisor, l2 // common_divisor)
if __name__ == '__main__':
    l1_val = 48
    l2_val = 18
    ratio = find_ratio_of_lengths(l1_val, l2_val)
    print(f"{l1_val}: {l2_val} -> {ratio[0]}: {ratio[1]}")
    l1_val = 101
    l2_val = 100
    ratio = find_ratio_of_lengths(l1_val, l2_val)
    print(f"{l1_val}: {l2_val} -> {ratio[0]}: {ratio[1]}")
    l1_val = 30
    l2_val = 6
    ratio = find_ratio_of_lengths(l1_val, l2_val)
    print(f"{l1_val}: {l2_val} -> {ratio[0]}: {ratio[1]}")
    l1_val = 17
    l2_val = 5
    ratio = find_ratio_of_lengths(l1_val, l2_val)
    print(f"{l1_val}: {l2_val} -> {ratio[0]}: {ratio[1]}")