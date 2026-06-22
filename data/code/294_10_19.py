def calculate_weight(density, volume):
    return density * volume

if __name__ == '__main__':
    sample_densities = [2.5, 3.0, 4.5]
    sample_volumes = [10, 20, 15]

    for density, volume in zip(sample_densities, sample_volumes):
        weight = calculate_weight(density, volume)
        print(f"Density: {density}, Volume: {volume}, Weight: {weight}")