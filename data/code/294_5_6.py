import math
def calculate_equivalent_weight(mass_of_element, molar_mass):
    return mass_of_element * (molar_mass / 100.0)
if __name__ == '__main__':
    mass_of_element = 5.0
    molar_mass = 32.0
    equivalent_weight = calculate_equivalent_weight(mass_of_element, molar_mass)
    print(equivalent_weight)