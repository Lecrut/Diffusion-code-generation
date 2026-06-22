class MassConverter:
    def __init__(self):
        self.kg_to_tons = 0.001

    def convert(self, kg: float) -> float:
        return round(kg * self.kg_to_tons, 3)

if __name__ == '__main__':
    converter = MassConverter()
    sample_kg = 2500
    tons = converter.convert(sample_kg)
    print(f"{tons} tons")