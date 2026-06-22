CONVERSION_FACTOR = 2.20462

def pounds_to_kilograms(pounds):
    return pounds / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_pounds = 35
    converted_kg = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is equal to {converted_kg:.2f} kg")