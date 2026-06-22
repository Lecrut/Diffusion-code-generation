CONVERSION_FACTOR = 2.20462

def pounds_to_kg(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Pounds must be a non-negative number")
    return pounds / CONVERSION_FACTOR

def kg_to_pounds(kilograms):
    if not isinstance(kilograms, (int, float)) or kilograms < 0:
        raise ValueError("Kilograms must be a non-negative number")
    return kilograms * CONVERSION_FACTOR

if __name__ == '__main__':
    pounds = 22.0462
    kilograms = 10
    converted_kg = kg_to_pounds(kilograms)
    print(f"{kilograms} kg is equal to {converted_kg:.2f} lbs")
    converted_pounds = pounds_to_kg(pounds)
    print(f"{pounds} lbs is equal to {converted_pounds:.2f} kg")