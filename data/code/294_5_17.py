def validate_mass(mass):
    if mass < 0:
        raise ValueError("Mass cannot be negative")

def calculate_equivalent_weight(mass_A, molar_mass_A, mass_B, molar_mass_B):
    validate_mass(mass_A)
    validate_mass(mass_B)
    
    molar_ratio = (molar_mass_B / molar_mass_A) ** 0.5
    equivalent_weight = mass_A * molar_ratio + mass_B
    
    return equivalent_weight

if __name__ == '__main__':
    mass_of_ch4 = 16.0
    molar_mass_of_ch4 = 16.04
    mass_of_c = 12.0
    molar_mass_of_c = 12.01
    
    try:
        equivalent_weight = calculate_equivalent_weight(mass_of_ch4, molar_mass_of_ch4, mass_of_c, molar_mass_of_c)
        print(f"Equivalent weight of CH4 and C: {equivalent_weight:.2f} g")
    except ValueError as e:
        print(f"Error: {e}")