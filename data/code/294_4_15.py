def calculate_equivalent_weight(mass, molecular_weight):
    return mass * (molecular_weight / 100)

if __name__ == '__main__':
    CO2_mass = 44.0
    CO2_molar_weight = 44.01
    equivalent_weight = calculate_equivalent_weight(CO2_mass, CO2_molar_weight)
    print(equivalent_weight)