import math
def calculate_new_denominator(numerator, denominator, target_numerator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    ratio = numerator / denominator
    new_denominator = target_numerator / ratio
    if abs(new_denominator - round(new_denominator)) < 1e-9:
        return int(round(new_denominator))
    else:
        return new_denominator
if __name__ == '__main__':
    num = 3
    den = 4
    target = 15
    result = calculate_new_denominator(num, den, target)
    print(f"Original Ratio (Numerator/Denominator): {num}/{den}")
    print(f"Target Numerator: {target}")
    print(f"New Denominator: {result}")