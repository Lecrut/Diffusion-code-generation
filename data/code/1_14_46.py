KG_TO_POUNDS_RATE = 2.20462

def convert_kg_to_pounds(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Weight in kilograms must be a non-negative number.")
    return kg * KG_TO_POUNDS_RATE

def convert_pounds_to_kg(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Weight in pounds must be a non-negative number.")
    return pounds / KG_TO_POUNDS_RATE

if __name__ == '__main__':
    sample_kg = 90
    sample_pounds = 198.426
    converted_pounds = convert_kg_to_pounds(sample_kg)
    converted_kg = convert_pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")