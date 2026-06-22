class MixtureCalculator:
    NH3_MOLAR_mass = 17.03
    H_MOLAR_mass = 1.01

    @staticmethod
    def calculate_equivalent_weights(masses):
        total_mass = sum(masses)
        weights = [mass / total_mass for mass in masses]
        return weights
if __name__ == '__main__':
    ammonia_mass = [17.03] * 1
    hydrogen_mass = [1.01] * 2
    total_masses = ammonia_mass + hydrogen_mass
    equivalent_weights = MixtureCalculator.calculate_equivalent_weights(total_masses)
    print(equivalent_weights)