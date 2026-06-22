class LengthConverter:
    def __init__(self):
        self.factors = {
            'meters': 1.0,
            'feet': 3.28084
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors or to_unit not in self.factors:
            raise ValueError("Unsupported unit")
        meters = value / self.factors[from_unit]
        result = meters * self.factors[to_unit]
        return result

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(100, 'meters', 'feet'))
    print(converter.convert(10, 'feet', 'meters'))