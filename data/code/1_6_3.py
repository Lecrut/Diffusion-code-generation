class WeightConverter:
    def __init__(self):
        self.weight = 0.0
        self.unit = 'lb'
    def set_weight(self, value, unit):
        self.weight = value
        self.unit = unit
    def convert_weight(self, target_unit):
        if self.unit == target_unit:
            return self.weight
        if self.unit == 'lb' and target_unit == 'kg':
            return self.weight * 0.453592
        elif self.unit == 'kg' and target_unit == 'lb':
            return self.weight / 0.453592
        elif self.unit == 'oz' and target_unit == 'lb':
            return self.weight / 16
        elif self.unit == 'lb' and target_unit == 'oz':
            return self.weight * 16
        elif self.unit == 'kg' and target_unit == 'oz':
            return self.weight * 35.27397
        else:
            raise ValueError("Unsupported conversion: from {} to {}".format(self.unit, target_unit))
if __name__ == '__main__':
    converter = WeightConverter()
    converter.set_weight(150, 'lb')
    print("Original weight:", converter.weight, converter.unit)
    kg_weight = converter.convert_weight('kg')
    print("Converted to kg:", kg_weight)
    converter.set_weight(75, 'kg')
    lb_weight = converter.convert_weight('lb')
    print("Converted to lb:", lb_weight)
    converter.set_weight(320, 'oz')
    lb_weight_from_oz = converter.convert_weight('lb')
    print("Converted from oz to lb:", lb_weight_from_oz)
    converter.set_weight(2, 'lb')
    oz_weight = converter.convert_weight('oz')
    print("Converted to oz:", oz_weight)