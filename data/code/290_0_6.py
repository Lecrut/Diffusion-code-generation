def validate_kilograms(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Kilograms must be a non-negative number")

def kg_to_pounds(kg):
    validate_kilograms(kg)
    return kg * 2.20462

if __name__ == '__main__':
    sample_values = [1, 5, 10, 1.5]
    for kg in sample_values:
        print(f"{kg} kg is equal to {kg_to_pounds(kg):.2f} pounds")