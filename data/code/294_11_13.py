def calculate_equivalent_weight(mass, volume):
    density_table = {
        'water': 1000,
        'aluminum': 2700,
        'gold': 19300
    }
    
    if isinstance(volume, dict):
        return {obj: mass / vol * density for obj, (vol, den) in volume.items() if den in density_table}
    else:
        return mass / volume * density_table.get('water', 1000)

if __name__ == '__main__':
    single_result = calculate_equivalent_weight(1.0, 'aluminum')
    print(f"Single result: {single_result}")
    
    multiple_results = calculate_equivalent_weight(1.5, {'water': (0.1, 1000), 'gold': (0.2, 19300)})
    print(f"Multiple results: {multiple_results}")