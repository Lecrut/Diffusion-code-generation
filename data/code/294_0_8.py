def calculate_equivalent_weight(mass1, molar_mass1, mass2, molar_mass2):
    return (mass1 / molar_mass1) + (mass2 / molar_mass2)

if __name__ == '__main__':
    print(calculate_equivalent_weight(2.0, 32.0, 4.0, 18.0))