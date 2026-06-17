def convert_grams_to_kilograms(masses_grams):
    masses_kilograms = []
    for mass in masses_grams:
        masses_kilograms.append(mass / 1000.0)
    return masses_kilograms
if __name__ == '__main__':
    sample_masses = [1500, 2500.5, 3000, 499.999]
    result_masses = convert_grams_to_kilograms(sample_masses)
    print(result_masses)