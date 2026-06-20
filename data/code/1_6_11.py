class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    def convert(self, new_unit):
        if self.unit == new_unit:
            return self.weight
        if self.unit == 'pounds' and new_unit == 'kilograms':
            return self.weight * 0.453592
        if self.unit == 'kilograms' and new_unit == 'pounds':
            return self.weight / 0.453592
        raise ValueError("Unsupported conversion")

if __name__ == '__main__':
    w = WeightConverter(10, 'pounds')
    result = w.convert('kilograms')
    print(result)