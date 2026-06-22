def calculate_equivalent_weight(mass, molar_mass):
    return mass / molar_mass
if __name__ == '__main__':
    mass_NH3 = 17.0
    molar_mass_NH3 = 17.03
    mass_H = 2.0
    molar_mass_H = 1.01
    weight_NH3 = calculate_equivalent_weight(mass_NH3, molar_mass_NH3)
    weight_H = calculate_equivalent_weight(mass_H, molar_mass_H)
    total_weight = weight_NH3 + weight_H
    print(f'Equivalent weight of NH3: {weight_NH3:.4f}')
    print(f'Equivalent weight of H: {weight_H:.4f}')
    print(f'Total equivalent weight: {total_weight:.4f}')