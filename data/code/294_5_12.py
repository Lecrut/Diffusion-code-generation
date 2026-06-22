class MixtureCalculator:
    MOLAR_MASS_CH4 = 16.04
    MOLAR_MASS_C = 12.01
    
    @staticmethod
    def calculate_equivalent_weight(mass, molar_mass):
        return mass * (molar_mass / 100.0)

if __name__ == '__main__':
    mass_ch4 = 16.0
    mass_c = 12.0
    equivalent_weight_ch4 = MixtureCalculator.calculate_equivalent_weight(mass_ch4, MixtureCalculator.MOLAR_MASS_CH4)
    equivalent_weight_c = MixtureCalculator.calculate_equivalent_weight(mass_c, MixtureCalculator.MOLAR_MASS_C)
    
    print(f"Equivalent weight of methane (CH4): {equivalent_weight_ch4:.2f} g")
    print(f"Equivalent weight of carbon (C): {equivalent_weight_c:.2f} g")