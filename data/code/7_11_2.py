class TimeConverter:
    def __init__(self):
        self.units = {
            's': 1,
            'sec': 1,
            'second': 1,
            'seconds': 1,
            'm': 60,
            'min': 60,
            'minute': 60,
            'minutes': 60,
            'h': 3600,
            'hr': 3600,
            'hour': 3600,
            'hours': 3600,
            'd': 86400,
            'day': 86400,
            'days': 86400,
            'w': 604800,
            'week': 604800,
            'weeks': 604800,
            'mo': 2592000,
            'month': 2592000,
            'months': 2592000,
            'y': 31536000,
            'yr': 31536000,
            'year': 31536000,
            'years': 31536000,
        }

    def _normalize_value(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            val, unit = value
            if val == 0:
                return 0
            unit_lower = str(unit).lower().strip()
            if unit_lower not in self.units:
                raise ValueError(f"Unknown unit: {unit}")
            return val * self.units[unit_lower]
        return float(value)

    def _to_seconds(self, value):
        return self._normalize_value(value)

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            val = self._normalize_value(value)
            return val
        seconds = self._to_seconds(value)
        if to_unit == 's' or to_unit == 'sec' or to_unit == 'second' or to_unit == 'seconds':
            return seconds
        target_factor = self.units.get(to_unit.lower())
        if target_factor is None:
            raise ValueError(f"Unknown target unit: {to_unit}")
        return seconds / target_factor

    def convert_tuple(self, value_tuple, to_unit):
        seconds = self._to_seconds(value_tuple)
        if to_unit == 's' or to_unit == 'sec' or to_unit == 'second' or to_unit == 'seconds':
            return seconds
        target_factor = self.units.get(to_unit.lower())
        if target_factor is None:
            raise ValueError(f"Unknown target unit: {to_unit}")
        return seconds / target_factor

if __name__ == '__main__':
    converter = TimeConverter()
    result1 = converter.convert(1, 'hours', 'minutes')
    result2 = converter.convert(3600, 'seconds', 'hours')
    result3 = converter.convert_tuple((2, 'days'), 'hours')
    result4 = converter.convert(1.5, 'hours', 'seconds')
    print(result1)
    print(result2)
    print(result3)
    print(result4)