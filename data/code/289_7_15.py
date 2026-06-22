def validate_input(ounces):
    if not isinstance(ounces, (int, float)) or ounces < 0:
        raise ValueError("Input must be a non-negative number")

def ounces_to_grams(ounces):
    grams = ounces * 28.3495
    return grams

if __name__ == '__main__':
    sample_ounces = 10
    try:
        validate_input(sample_ounces)
        grams_result = ounces_to_grams(sample_ounces)
        print(f"Input ounces: {sample_ounces}")
        print(f"Result in grams: {grams_result}")
    except ValueError as e:
        print(e)