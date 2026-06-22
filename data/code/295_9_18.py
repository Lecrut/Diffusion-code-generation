def validate_weight(value):
    if value < 0:
        raise ValueError("Weight must be non-negative")
    return value

def pounds_to_kg(lbs):
    return validate_weight(lbs) / 2.20462

if __name__ == '__main__':
    pounds = 150
    kilograms = pounds_to_kg(pounds)
    print(f"{pounds} lbs is equal to {kilograms:.2f} kg")