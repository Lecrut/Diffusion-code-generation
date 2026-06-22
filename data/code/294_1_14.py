class WaterMolecularWeight:
    def __init__(self):
        self.water_mass = 18.0
        self.oxygen_atomic_mass = 16.0

    def calculate_equivalent_weight(self, component_masses, molecular_weights):
        total_equivalent_weight = 0.0
        for mass, mw in zip(component_masses, molecular_weights):
            if mw != 0:
                equivalent_weight = mass / mw
                total_equivalent_weight += equivalent_weight
        return total_equivalent_weight

if __name__ == '__main__':
    water_instance = WaterMolecularWeight()
    component_masses = [18.0, 32.0, 44.0]
    molecular_weights = [18.015, 16.00, 18.015]
    result = water_instance.calculate_equivalent_weight(component_masses, molecular_weights)
    print(result)