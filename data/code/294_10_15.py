class MaterialWeightCalculator:
    def __init__(self):
        self.densities = {}
    
    def add_material(self, material, density):
        if material not in self.densities:
            self.densities[material] = density
        else:
            raise ValueError(f"Material {material} already exists.")
    
    def calculate_weight(self, volume, material):
        if material not in self.densities:
            raise KeyError(f"Material {material} not found.")
        return volume * self.densities[material]

if __name__ == '__main__':
    calculator = MaterialWeightCalculator()
    calculator.add_material('water', 1.0)
    calculator.add_material('gold', 19.32)
    
    water_weight = calculator.calculate_weight(1.0, 'water')
    gold_weight = calculator.calculate_weight(1.0, 'gold')
    
    print(f"Weight of 1m³ of water: {water_weight} kg")
    print(f"Weight of 1m³ of gold: {gold_weight} kg")