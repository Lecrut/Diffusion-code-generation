import math
def calculate_equivalent_weight(mass_of_element, molar_mass):
    return mass_of_element * (molar_mass / 100.0)
if __name__ == '__main__':
    mass_of_element = 10.0
    molar_mass = 16.0                   
    equivalent_weight = calculate_equivalent_weight(mass_of_element, molar_mass)
    print(f"Mass of element: {mass_of_element}")
    print(f"Molar mass: {molar_mass}")
    print(f"Equivalent weight: {equivalent_weight}")