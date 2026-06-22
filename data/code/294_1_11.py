def calculate_equivalent_weight(mass, molar_mass):
    return mass / molar_mass

if __name__ == '__main__':
    water_mass = 18.0
    oxygen_atomic_mass = 16.0
    H2O_molar_mass = 18.015
    
    equivalent_weight_H2O = calculate_equivalent_weight(water_mass, H2O_molar_mass)
    
    print(equivalent_weight_H2O)