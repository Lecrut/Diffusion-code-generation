def calculate_weight(density, volume):
    return density * volume

if __name__ == '__main__':
    sample_densities = [2.5, 3.0, 4.5]
    sample_volumes = [10, 20, 30]

    for density, volume in zip(sample_densities, sample_volumes):
        weight = calculate_weight(density, volume)
        print(f"Material with density {density} g/cm³ and volume {volume} cm³ has a weight of {weight} g")