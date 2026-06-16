def convert_grams_to_kilograms(masses_grams):
    masses_kilograms = []
    for mass in masses_grams:
        mass_kg = mass / 1000.0
        masses_kilograms.append(mass_kg)
    return masses_kilograms
if __name__ == '__main__':
    sample_masses = [1500, 2500.5, 3000, 4567.89]
    result_masses = convert_grams_to_kilograms(sample_masses)
    print(result_masses)