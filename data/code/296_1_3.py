import math
def change_ratio(numerator, denominator, scale):
    new_numerator = numerator * scale
    new_denominator = denominator * scale
    common_divisor = math.gcd(new_numerator, new_denominator)
    simplified_numerator = new_numerator // common_divisor
    simplified_denominator = new_denominator // common_divisor
    return simplified_numerator, simplified_denominator
if __name__ == '__main__':
    initial_num = 10
    initial_den = 15
    scale_factor = 3
    new_num, new_den = change_ratio(initial_num, initial_den, scale_factor)
    print(f"{new_num}/{new_den}")
    initial_num = 2
    initial_den = 4
    scale_factor = 5
    new_num, new_den = change_ratio(initial_num, initial_den, scale_factor)
    print(f"{new_num}/{new_den}")
    initial_num = 12
    initial_den = 8
    scale_factor = 2
    new_num, new_den = change_ratio(initial_num, initial_den, scale_factor)
    print(f"{new_num}/{new_den}")