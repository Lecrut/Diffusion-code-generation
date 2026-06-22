def calculate_equivalent_weight(mass, volume):
    density = mass / volume
    return density
if __name__ == '__main__':
    sample_masses = [50, 75, 100]
    sample_volumes = [2, 3, 4]
    for i in range(len(sample_masses)):
        print(f'Object {i + 1} equivalent weight: {calculate_equivalent_weight(sample_masses[i], sample_volumes[i]):.2f} kg/m^3')