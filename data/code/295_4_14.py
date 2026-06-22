def kg_to_pounds(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Invalid input for kilograms. Must be a non-negative number.")
    return round(kg * 2.20462, 3)

if __name__ == '__main__':
    sample_kg = 10.0
    pounds = kg_to_pounds(sample_kg)
    print(f"{sample_kg} kilograms is equal to {pounds:.3f} pounds")