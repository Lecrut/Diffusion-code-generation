def calculate_equivalent_weight(masses, volumes):
    densities = [mass / volume for mass, volume in zip(masses, volumes)]
    equivalent_weights = [1 / density for density in densities]
    return equivalent_weights
if __name__ == '__main__':
    masses = [20, 30, 40]
    volumes = [5, 10, 15]
    results = calculate_equivalent_weight(masses, volumes)
    print(results)