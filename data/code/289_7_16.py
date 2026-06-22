CONVERSION_FACTOR = {
    'ounces': 28.3495
}

def convert_ounces_to_grams(ounces):
    if not isinstance(ounces, (int, float)):
        raise ValueError("Invalid input: Ounces must be a number")
    return ounces * CONVERSION_FACTOR['ounces']

if __name__ == '__main__':
    sample_ounces = 10
    grams_result = convert_ounces_to_grams(sample_ounces)
    print(f"Input ounces: {sample_ounces}")
    print(f"Result in grams: {grams_result}")