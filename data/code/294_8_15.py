BA_CL2_MOLAR_MASS = 207.2
CL_ATOMIC_MASS = 35.45

def calculate_equivalent_weight(mass_bacl2):
    return mass_bacl2 / (BA_CL2_MOLAR_MASS - 2 * CL_ATOMIC_MASS)

if __name__ == '__main__':
    sample_mass = 207
    result = calculate_equivalent_weight(sample_mass)
    print(result)