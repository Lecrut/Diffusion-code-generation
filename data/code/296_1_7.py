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
    scale_factor = 4
    result_num, result_den = change_ratio(initial_num, initial_den, scale_factor)
    print(f"Initial Ratio: {initial_num}/{initial_den}, Scale Factor: {scale_factor}")
    print(f"New Simplified Ratio: {result_num}/{result_den}")
    initial_num = 21
    initial_den = 35
    scale_factor = 2
    result_num, result_den = change_ratio(initial_num, initial_den, scale_factor)
    print(f"Initial Ratio: {initial_num}/{initial_den}, Scale Factor: {scale_factor}")
    print(f"New Simplified Ratio: {result_num}/{result_den}")
    initial_num = 100
    initial_den = 50
    scale_factor = 3
    result_num, result_den = change_ratio(initial_num, initial_den, scale_factor)
    print(f"Initial Ratio: {initial_num}/{initial_den}, Scale Factor: {scale_factor}")
    print(f"New Simplified Ratio: {result_num}/{result_den}")