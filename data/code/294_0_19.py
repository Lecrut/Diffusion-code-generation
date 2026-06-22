def calculate_equivalent_weight(mass1, molar_mass1, mass2, molar_mass2):
    return (mass1 / molar_mass1) + (mass2 / molar_mass2)

if __name__ == '__main__':
    print(calculate_equivalent_weight(10.0, 32.065, 20.0, 40.08))