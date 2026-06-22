conversion_factors = {
    'mm': 0.0393701
}

def millimeters_to_inches(millimeters):
    if not isinstance(millimeters, (int, float)):
        raise TypeError("Input must be a number.")
    return millimeters * conversion_factors['mm']

if __name__ == '__main__':
    sample_value = 254
    try:
        inches = millimeters_to_inches(sample_value)
        print(f"{sample_value} mm is equal to {inches} in")
    except TypeError as e:
        print(e)