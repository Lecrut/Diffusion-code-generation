def calculate_equivalent_weight(mass_of_element, molar_mass):
    return mass_of_element * (molar_mass / 100.0)

if __name__ == '__main__':
    element_info = {
        'CH4': {'mass': 16.04, 'symbol': 'methane'},
        'C': {'mass': 12.01, 'symbol': 'carbon'}
    }
    
    mass_CH4 = 16.0
    mass_C = 12.0
    
    equivalent_weight_CH4 = calculate_equivalent_weight(mass_CH4, element_info['CH4']['mass'])
    equivalent_weight_C = calculate_equivalent_weight(mass_C, element_info['C']['mass'])
    
    print(f"Equivalent weight of CH4: {equivalent_weight_CH4:.2f}")
    print(f"Equivalent weight of C: {equivalent_weight_C:.2f}")