def validate_length(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise TypeError("length must be numeric")
    if kilometers < 0:
        raise ValueError("length cannot be negative")
    return float(kilometers)


def convert_kilometers_to_miles(kilometers):
    length_kilometers = validate_length(kilometers)
    return length_kilometers * 0.621371


if __name__ == '__main__':
    sample_length_kilometers = 25.0
    conversion_result_miles = convert_kilometers_to_miles(sample_length_kilometers)
    print(f"{sample_length_kilometers} kilometers = {conversion_result_miles:.3f} miles")
