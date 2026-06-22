def calculate_weight(density, volume):
    return density * volume
if __name__ == '__main__':
    materials = {'water': (1000, 2), 'aluminum': (2700, 0.5), 'gold': (19300, 0.1)}
    for material, (density, volume) in materials.items():
        weight = calculate_weight(density, volume)
        print(f'The weight of {material} is {weight} kg')