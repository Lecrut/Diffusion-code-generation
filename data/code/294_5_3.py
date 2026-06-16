import math
def calculate_equivalent_weight(mass_of_element, molar_mass):
    return mass_of_element * (molar_mass / 100.0)
if __name__ == '__main__':
    mass_of_iron = 44.0
    molar_mass_iron = 55.845
    equivalent_weight_iron = calculate_equivalent_weight(mass_of_iron, molar_mass_iron)
    print(f"Mass of Iron: {mass_of_iron} g")
    print(f"Molar Mass of Iron: {molar_mass_iron} g/mol")
    print(f"Equivalent Weight of Iron (based on 1 mole): {equivalent_weight_iron:.2f} g")