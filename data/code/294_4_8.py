class CarbonDioxide:
    def __init__(self, mass):
        self.mass = mass

    def calculate_equivalent_weight(self, molecular_weight):
        return self.mass * (molecular_weight / 100.0)

if __name__ == '__main__':
    co2_instance = CarbonDioxide(44)
    molecular_weight_sample = 44.01
    equivalent_weight = co2_instance.calculate_equivalent_weight(molecular_weight_sample)
    print(equivalent_weight)