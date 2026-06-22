class ObjectWeightCalculator:
    @staticmethod
    def calculate_weight(mass, volume):
        return mass / volume

if __name__ == '__main__':
    sample_masses = [10.0, 20.0, 30.0]
    sample_volumes = [1.0, 2.0, 3.0]

    calculator = ObjectWeightCalculator()
    weights = [calculator.calculate_weight(mass, volume) for mass, volume in zip(sample_masses, sample_volumes)]

    print(weights)