CONVERSION_FACTOR = 2.20462

def kg_to_pounds(kg):
    return kg * CONVERSION_FACTOR

def pounds_to_kg(pounds):
    return pounds / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kg_values = [70, 85, 90]
    sample_pounds_values = [154, 187, 200]
    
    for kg in sample_kg_values:
        converted_pounds = kg_to_pounds(kg)
        print(f"{kg} kg is {converted_pounds:.2f} pounds")
    
    for pounds in sample_pounds_values:
        converted_kg = pounds_to_kg(pounds)
        print(f"{pounds} pounds is {converted_kg:.2f} kg")