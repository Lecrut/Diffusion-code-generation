class Weight:
    def __init__(self, value, unit='kg'):
        self.value = value
        self.unit = unit

    def convert_to(self, target_unit):
        if self.unit == target_unit:
            return self.value
        
        if self.unit == 'kg' and target_unit == 'lbs':
            return self.value * 2.20462
        if self.unit == 'lbs' and target_unit == 'kg':
            return self.value / 2.20462
        
        raise ValueError(f"Conversion from {self.unit} to {target_unit} is not supported.")

    def __repr__(self):
        return f"{self.value} {self.unit}"

if __name__ == '__main__':
    weight_obj = Weight(10, 'kg')
    result = weight_obj.convert_to('lbs')
    print(f"Original: {weight_obj}")
    print(f"Converted: {result}")