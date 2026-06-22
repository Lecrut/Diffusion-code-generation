def validate_inputs(mass, moles, atomic_weight):
    if not (isinstance(mass, (int, float)) and isinstance(moles, (int, float)) and isinstance(atomic_weight, (int, float))):
        raise ValueError("All inputs must be numeric values.")

def calculate_equivalent_weight(mass, moles, atomic_weight):
    validate_inputs(mass, moles, atomic_weight)
    return mass / moles * atomic_weight

if __name__ == '__main__':
    mass_val = 100.0
    moles_val = 2.5
    atomic_weight_val = 50.0
    equivalent_weight = calculate_equivalent_weight(mass_val, moles_val, atomic_weight_val)
    print(equivalent_weight)