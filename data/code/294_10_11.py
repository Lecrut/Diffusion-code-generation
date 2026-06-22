class Material:

    def __init__(self):
        self.density = {}

    def add_material(self, formula, density):
        self.density[formula] = density

    def calculate_weight(self, volume, formula):
        if formula not in self.density:
            raise ValueError(f'Material {formula} not found')
        return volume * self.density[formula]
if __name__ == '__main__':
    material = Material()
    material.add_material('H2O', 1.0)
    material.add_material('Fe', 7.874)
    print(material.calculate_weight(1.0, 'H2O'))
    print(material.calculate_weight(0.5, 'Fe'))