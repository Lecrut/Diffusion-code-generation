def validate_weight(weight_pounds):
    if weight_pounds < 0:
        raise ValueError("Weight cannot be negative")
    return weight_pounds

def convert_pounds_to_kilograms(weight_pounds):
    return round(weight_pounds * 0.453592, 1)

if __name__ == '__main__':
    sample_weight = -5
    try:
        validated_weight = validate_weight(sample_weight)
        result = convert_pounds_to_kilograms(validated_weight)
        print(result)
    except ValueError as e:
        print(e)