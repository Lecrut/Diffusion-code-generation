def calculate_new_denominator(numerator_ratio, denominator_ratio, target_numerator):
    if denominator_ratio == 0:
        raise ValueError("Denominator ratio cannot be zero.")
    if numerator_ratio == 0:
        if target_numerator == 0:
            return 0
        else:
            raise ValueError("Cannot change the relationship if original numerator is zero and target is non-zero.")
    new_denominator = (target_numerator * denominator_ratio) / numerator_ratio
    if new_denominator == int(new_denominator):
        return int(new_denominator)
    else:
        return new_denominator
if __name__ == '__main__':
    numerator = 3
    denominator = 4
    target = 15
    try:
        result = calculate_new_denominator(numerator, denominator, target)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")