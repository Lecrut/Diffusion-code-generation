class TimeConverter:
    def __init__(self):
        self._units = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800,
            'years': 31536000
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._units:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        seconds = value * self._units[from_unit]
        result = seconds / self._units[to_unit]
        return result

    def to_seconds(self, value, from_unit):
        if from_unit not in self._units:
            raise ValueError(f"Unknown unit: {from_unit}")
        return value * self._units[from_unit]

    def from_seconds(self, value, to_unit):
        if to_unit not in self._units:
            raise ValueError(f"Unknown unit: {to_unit}")
        return value / self._units[to_unit]

if __name__ == '__main__':
    converter = TimeConverter()
    result = converter.convert(3600, 'seconds', 'hours')
    print(result)
    
    seconds_result = converter.to_seconds(2, 'hours')
    print(seconds_result)
    
    minutes_result = converter.from_seconds(3600, 'minutes')
    print(minutes_result)