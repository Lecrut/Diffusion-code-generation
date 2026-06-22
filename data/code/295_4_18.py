def is_valid_kg(kg):
    if kg is None or not isinstance(kg, (int, float)) or kg < 0:
        return False
    return True

def kg_to_pounds(kg):
    if not is_valid_kg(kg):
        raise ValueError("Invalid input for kilograms. Must be a non-negative number.")
    pounds = kg * 2.20462
    return round(pounds, 3)

if __name__ == '__main__':
    sample_kg = 10.0
    print(f"{sample_kg} kg is equal to {kg_to_pounds(sample_kg)} lbs")