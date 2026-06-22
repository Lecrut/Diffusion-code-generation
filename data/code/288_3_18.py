def validate_celsius(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number")
    return celsius

def celsius_to_reaumur(celsius):
    return validate_celsius(celsius) * 4 / 5

if __name__ == '__main__':
    sample_celsius = -10
    result = celsius_to_reaumur(sample_celsius)
    print(result)