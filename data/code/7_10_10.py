class TimeConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()
        self.valid_units = ['seconds', 'minutes', 'hours', 'days']
        
        if self.unit not in self.valid_units:
            raise ValueError(f"Unit must be one of {self.valid_units}")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Value must be a non-negative number")

    def _to_seconds(self, value, unit):
        conversions = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }
        return value * conversions[unit]

    def convert(self):
        base_seconds = self._to_seconds(self.value, self.unit)
        result = {}
        conversions = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }
        
        for unit_name, divisor in conversions.items():
            if unit_name == self.unit:
                result[unit_name] = self.value
            else:
                converted_val = base_seconds / divisor
                if converted_val.is_integer():
                    result[unit_name] = int(converted_val)
                else:
                    result[unit_name] = round(converted_val, 4)
        return result

if __name__ == '__main__':
    converter = TimeConverter(2.5, 'hours')
    output = converter.convert()
    print(output)