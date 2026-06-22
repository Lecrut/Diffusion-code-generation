def calculate_equivalent_weight(molar_mass, quantity):
    return molar_mass * quantity
if __name__ == '__main__':
    substance_data = [(100.0, 2.5), (18.015, 2.0), (44.01, 1.0)]
    for molar_mass, quantity in substance_data:
        equivalent_weight = calculate_equivalent_weight(molar_mass, quantity)
        print(f'Molar Mass: {molar_mass} g/mol')
        print(f'Quantity: {quantity}')
        print(f'Equivalent Weight: {equivalent_weight} g/mol')