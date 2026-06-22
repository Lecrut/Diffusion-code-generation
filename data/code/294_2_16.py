def equivalent_weights(masses, molar_masses):
    return [mass / molar_mass for mass, molar_mass in zip(masses, molar_masses)]

if __name__ == '__main__':
    masses = [10.0, 20.0, 30.0]
    molar_masses = [16.0, 32.0, 48.0]
    print(equivalent_weights(masses, molar_masses))