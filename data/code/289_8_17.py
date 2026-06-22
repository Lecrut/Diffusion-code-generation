class WeightConverter:

    def __init__(self):
        self.conversions = {'lb': 0.453592}

    def convert_to_kg(self, value):
        if 'lb' in self.conversions:
            return f'{value * self.conversions['lb']:.2f}'
        else:
            raise ValueError('Unsupported unit: lb')
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.convert_to_kg(10))
    print(converter.convert_to_kg(20))