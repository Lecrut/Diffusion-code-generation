class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def change_unit(self, new_unit):
        if self.unit == new_unit:
            return self.value, self.unit
        
        if self.unit == 'lb' and new_unit == 'kg':
            return self.value * 0.45359237, new_unit
        elif self.unit == 'kg' and new_unit == 'lb':
            return self.value / 0.45359237, new_unit
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    w = Weight(100, 'lb')
    result_value, result_unit = w.change_unit('kg')
    print(result_value, result_unit)
    w2 = Weight(50, 'kg')
    result_value2, result_unit2 = w2.change_unit('lb')
    print(result_value2, result_unit2)