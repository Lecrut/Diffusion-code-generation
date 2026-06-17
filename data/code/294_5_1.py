import math
def calculate_equivalent_weight(mass_A, moles_B, stoichiometry):
    if stoichiometry == 0:
        raise ValueError("Stoichiometry cannot be zero")
    equivalent_mass = mass_A * stoichiometry
    return equivalent_mass / moles_B
if __name__ == '__main__':
    mass_A = 10.0
    moles_B = 2.0
    stoichiometry = 2.0
    try:
        result = calculate_equivalent_weight(mass_A, moles_B, stoichiometry)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")