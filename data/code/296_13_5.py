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
    target = 12
    result = calculate_new_denominator(num, den, target)
    print(f"Original ratio: {num}/{den}")
    print(f"Target numerator: {target}")
    print(f"New denominator: {result}")