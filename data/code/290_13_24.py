def tons_to_kilograms(tons):
    conversion_factor = 907.184
    kilograms = tons * conversion_factor
    return round(kilograms, 2)

if __name__ == '__main__':
    sample_values = {1: 907.18, 2: 1814.368, 5: 4535.92}
    for tons, expected in sample_values.items():
        result = tons_to_kilograms(tons)
        print(f"{tons} ton(s) is approximately {result} kg (Expected: {expected})")