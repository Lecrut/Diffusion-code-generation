import numpy as np
def calculate_equivalent_weight(mass, moles, atomic_weight):
    return mass / moles * atomic_weight
if __name__ == '__main__':
    mass_val = 100.0
    moles_val = 2.5
    atomic_weight_val = 50.0
    result = calculate_equivalent_weight(mass_val, moles_val, atomic_weight_val)
    print(result)