def calculate_equivalent_weights(materials):
    density_volume = {'Steel': (7850, 1), 'Concrete': (2400, 1), 'Aluminum': (2700, 1), 'Copper': (8960, 1)}
    equivalent_weights = {}
    for material, (density, volume) in density_volume.items():
        if density > 0 and volume > 0:
            equivalent_weight = density * volume
        else:
            equivalent_weight = None
        equivalent_weights[material] = equivalent_weight
    return equivalent_weights
if __name__ == '__main__':
    sample_materials = {'Steel': (7850, 1), 'Concrete': (2400, 1), 'Aluminum': (2700, 1), 'Copper': (8960, 1)}
    weights = calculate_equivalent_weights(sample_materials)
    for material, weight in weights.items():
        print(f'{material}: {weight} kg')