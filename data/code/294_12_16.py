def validate_input(molar_mass, quantity):
    if molar_mass <= 0 or quantity <= 0:
        raise ValueError("Molar mass and quantity must be positive values.")

def calculate_equivalent_weight(molar_mass, quantity):
    validate_input(molar_mass, quantity)
    return molar_mass * quantity

if __name__ == '__main__':
    sample_substances = [
        {"molar_mass": 100.0, "quantity": 2.5},
        {"molar_mass": 18.015, "quantity": 3.0},
        {"molar_mass": 44.01, "quantity": 1.5}
    ]
    
    for substance in sample_substances:
        equivalent_weight = calculate_equivalent_weight(substance["molar_mass"], substance["quantity"])
        print(f"Substance Molar Mass: {substance['molar_mass']}, Quantity: {substance['quantity']}")
        print(f"Equivalent Weight: {equivalent_weight}\n")