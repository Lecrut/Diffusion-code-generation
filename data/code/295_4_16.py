def kg_to_lb(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Invalid input for kilograms. Must be a non-negative number.")
    return round(kg * 2.20462, 3)

if __name__ == '__main__':
    sample_kg = 5.0
    print(f"{sample_kg} kg is equal to {kg_to_lb(sample_kg):.3f} lbs")