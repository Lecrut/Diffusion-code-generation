def validate_ounces(ounces):
    if not isinstance(ounces, (int, float)) or ounces < 0:
        raise ValueError("Invalid input: Ounces must be a non-negative number")

def convert_ounces_to_grams(ounces):
    grams = ounces * 28.3495
    return grams

if __name__ == '__main__':
    sample_ounces = 10
    try:
        validate_ounces(sample_ounces)
        grams_result = convert_ounces_to_grams(sample_ounces)
        print(f"Input ounces: {sample_ounces}")
        print(f"Result in grams: {grams_result}")
    except ValueError as e:
        print(e)