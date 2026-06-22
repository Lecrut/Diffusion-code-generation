def convert_ounces_to_grams(ounces):
    if not isinstance(ounces, (int, float)) or ounces < 0:
        raise ValueError("Input must be a non-negative number")
    grams = ounces * 28.3495
    return grams

if __name__ == '__main__':
    sample_ounces = 10
    try:
        grams_result = convert_ounces_to_grams(sample_ounces)
        print(f"Input ounces: {sample_ounces}")
        print(f"Result in grams: {grams_result}")
    except ValueError as e:
        print(e)