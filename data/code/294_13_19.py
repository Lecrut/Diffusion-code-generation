def calculate_equivalent_weight(masses, volumes):
    if not masses or not volumes:
        raise ValueError("Masses and volumes must not be empty")
    
    densities = [mass / volume for mass, volume in zip(masses, volumes)]
    min_density_index = densities.index(min(densities))
    equivalent_weight = masses[min_density_index] * (volumes[min_density_index] / volumes[0])
    
    return equivalent_weight

if __name__ == '__main__':
    masses = [1.5, 2.0, 3.5]
    volumes = [0.5, 0.75, 1.0]
    print(calculate_equivalent_weight(masses, volumes))