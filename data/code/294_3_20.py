class ChemicalMixture:
    H2_MASS = 2.016
    O2_MASS = 32.0

    @staticmethod
    def calculate_equivalent_weight(mass_h2, mass_o2):
        total_mass = mass_h2 + mass_o2
        if total_mass == 0:
            raise ValueError('Total mass must be greater than zero.')
        moles_h2 = mass_h2 / ChemicalMixture.H2_MASS
        moles_o2 = mass_o2 / ChemicalMixture.O2_MASS
        equivalent_weight = (moles_h2 * ChemicalMixture.H2_MASS + moles_o2 * ChemicalMixture.O2_MASS) / total_mass
        return equivalent_weight
if __name__ == '__main__':
    sample_h2_mass = 2.0
    sample_o2_mass = 32.0
    try:
        result = ChemicalMixture.calculate_equivalent_weight(sample_h2_mass, sample_o2_mass)
        print(f'Equivalent weight of the mixture: {result:.4f} g/mol')
    except ValueError as e:
        print(e)