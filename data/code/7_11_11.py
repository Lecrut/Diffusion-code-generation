class TimeConverter:
    def __init__(self):
        self.units = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800,
            'months': 2592000,
            'years': 31536000,
            'milliseconds': 0.001,
            'microseconds': 0.000001,
            'nanoseconds': 0.000000001
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError(f"Invalid unit: {from_unit} or {to_unit}")
        
        base_value = value * self.units[from_unit]
        result = base_value / self.units[to_unit]
        
        return result

if __name__ == '__main__':
    converter = TimeConverter()
    
    result = converter.convert(3600, 'seconds', 'hours')
    print(result)
    
    result2 = converter.convert(1, 'days', 'hours')
    print(result2)
    
    result3 = converter.convert(1000, 'milliseconds', 'seconds')
    print(result3)