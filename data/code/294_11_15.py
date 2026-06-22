class ObjectWeightCalculator:
    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume

    def calculate_density(self):
        return self.mass / self.volume

    def calculate_equivalent_weight(self, atomic_weight):
        density = self.calculate_density()
        return density * atomic_weight

if __name__ == '__main__':
    object1 = ObjectWeightCalculator(mass=100.0, volume=5.0)
    print(f"Density of object 1: {object1.calculate_density()}")
    print(f"Equivalent weight of object 1 with atomic weight 50.0: {object1.calculate_equivalent_weight(50.0)}")