import math
def calculate_new_denominator(numerator_ratio, denominator_ratio, target_numerator):
    if denominator_ratio == 0:
        raise ValueError("Denominator ratio cannot be zero.")
    if numerator_ratio == 0:
        if target_numerator == 0:
            return 0
        else:
            raise ValueError("Cannot determine a unique denominator when the original numerator ratio is zero and the target is non-zero.")
    new_denominator = (target_numerator * denominator_ratio) / numerator_ratio
    if abs(new_denominator - round(new_denominator)) < 1e-9:
        return int(round(new_denominator))
    else:
        return new_denominator
if __name__ == '__main__':
    numerator = 3
    denominator = 4
    target = 15
    result = calculate_new_denominator(numerator, denominator, target)
    print(result)