def calculate_equivalent_weight(molar_mass, quantity):
    return molar_mass * quantity

if __name__ == '__main__':
    substance_data = [
        {'molar_mass': 18.015, 'quantity': 2.0},
        {'molar_mass': 44.01, 'quantity': 1.0}
    ]

    for data in substance_data:
        molar_mass_substance = data['molar_mass']
        quantity_substance = data['quantity']
        equivalent_weight = calculate_equivalent_weight(molar_mass_substance, quantity_substance)
        print(f"Equivalent weight (Molar Mass={molar_mass_substance}, Quantity={quantity_substance}): {equivalent_weight}")