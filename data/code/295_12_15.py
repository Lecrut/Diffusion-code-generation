def validate_pounds(pounds):
    if pounds < 0:
        raise ValueError("Pounds cannot be negative.")
    return pounds

def convert_pounds_to_kilograms(pounds):
    kilograms = pounds * 0.453592
    return kilograms

if __name__ == '__main__':
    sample_pounds = 10.0
    validated_pounds = validate_pounds(sample_pounds)
    kilograms_result = convert_pounds_to_kilograms(validated_pounds)
    print(f"{sample_pounds} pounds is {kilograms_result} kilograms")