def validate_weight(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Weight must be a number.")
    if value < 0:
        raise ValueError("Weight cannot be negative.")

def kg_to_pounds(kg):
    validate_weight(kg)
    return kg * 2.2046226218487757

def pounds_to_kg(pounds):
    validate_weight(pounds)
    return pounds / 2.2046226218487757

if __name__ == '__main__':
    sample_kg = 65
    sample_pounds = 143
    try:
        converted_pounds = kg_to_pounds(sample_kg)
        converted_kg = pounds_to_kg(sample_pounds)
        print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
        print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
    except ValueError as e:
        print(e)