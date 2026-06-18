class LengthConverter:
    def to_meters(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Input must be a positive number.")
        return value * self._get_factor('m')
    def from_meters(self, meters_value):
        if not isinstance(meters_value, (int, float)) or meters_value <= 0:
            raise ValueError("Input must be a positive number.")
        return meters_value / self._get_factor('m')
    def to_kilometers(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Input must be a positive number.")
        return value * self._get_factor('km')
    def from_kilometers(self, km_value):
        if not isinstance(km_value, (int, float)) or km_value <= 0:
            raise ValueError("Input must be a positive number.")
        return km_value / self._get_factor('km')
    def to_centimeters(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Input must be a positive number.")
        return value * self._get_factor('cm')
    def from_centimeters(self, cm_value):
        if not isinstance(cm_value, (int, float)) or cm_value <= 0:
            raise ValueError("Input must be a positive number.")
        return cm_value / self._get_factor('cm')
    def to_millimeters(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Input must be a positive number.")
        return value * self._get_factor('mm')
    def from_millimeters(self, mm_value):
        if not isinstance(mm_value, (int, float)) or mm_value <= 0:
            raise ValueError("Input must be a positive number.")
        return mm_value / self._get_factor('mm')
    def _get_factor(self, unit):
        factors = {
            'm': 1.0,
            'km': 0.001,
            'cm': 100.0,
            'mm': 1000.0
        }
        return factors.get(unit)
if __name__ == '__main__':
    converter = LengthConverter()
    print(f"{converter.to_meters(5)}")                                                                       
    pass