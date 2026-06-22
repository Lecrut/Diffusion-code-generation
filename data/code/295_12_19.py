def validate_pounds(pounds):
    if pounds < 0:
        raise ValueError("Pounds must be non-negative")

def convert_to_kilograms(pounds):
    validate_pounds(pounds)
    return pounds * 0.453592

if __name__ == '__main__':
    sample_pounds = 10.0
    kilograms_result = convert_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {kilograms_result} kg")