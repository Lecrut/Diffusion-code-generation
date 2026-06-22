def calculate_equivalent_weight(mass, molar_mass):
    return mass / molar_mass

def calculate_total_molar_mass(masses, molar_masses):
    if len(masses) != len(molar_masses):
        raise ValueError("The number of masses must match the number of molar masses.")
    
    total_mass = sum(masses)
    total_molar_mass = sum(mass * molar_mass for mass, molar_mass in zip(masses, molar_masses))
    
    return total_mass, total_molar_mass

def calculate_equivalent_weights(masses, molar_masses):
    if not masses or not molar_masses:
        raise ValueError("Masses and molar masses lists must be non-empty.")
    
    total_mass, total_molar_mass = calculate_total_molar_mass(masses, molar_masses)
    
    equivalent_weights = [mass * molar_mass / total_molar_mass for mass, molar_mass in zip(masses, molar_masses)]
    
    return equivalent_weights

if __name__ == '__main__':
    ammonia_mass = 17.0
    hydrogen_mass = 2.0
    
    ammonia_molar_mass = 17.03
    hydrogen_molar_mass = 1.01
    
    masses = [ammonia_mass, hydrogen_mass]
    molar_masses = [ammonia_molar_mass, hydrogen_molar_mass]
    
    equivalent_weights = calculate_equivalent_weights(masses, molar_masses)
    print(equivalent_weights)