CONVERSION_CONSTANT = 2.2046226218487757

def kg_to_pounds(kg):
    return kg * CONVERSION_CONSTANT

def pounds_to_kg(pounds):
    return pounds / CONVERSION_CONSTANT

if __name__ == '__main__':
    sample_kg = 65
    sample_pounds = 143.29
    converted_pounds = kg_to_pounds(sample_kg)
    converted_kg = pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")