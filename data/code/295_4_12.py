def kg_to_pounds(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Invalid input for kilograms. Must be a non-negative number.")
    pounds = kg * 2.20462
    return round(pounds, 3)

if __name__ == '__main__':
    sample_kg = 10.0
    print(f"{sample_kg} kilograms is equal to {kg_to_pounds(sample_kg):.3f} pounds")