CONVERSION_FACTOR = 2.20462

def kg_to_pounds(kg):
    return kg * CONVERSION_FACTOR

def pounds_to_kg(pounds):
    return pounds / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kg = 90
    sample_pounds = 198
    converted_pounds = kg_to_pounds(sample_kg)
    converted_kg = pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")