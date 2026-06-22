def validate_weight(weight_pounds):
    if weight_pounds < 0:
        raise ValueError("Weight cannot be negative")
    return True

def convert_pounds_to_kilograms(weight_pounds):
    if not validate_weight(weight_pounds):
        return None
    return round(weight_pounds * 0.453592, 1)

if __name__ == '__main__':
    sample_weight = 150.5
    result_weight = convert_pounds_to_kilograms(sample_weight)
    print(result_weight)