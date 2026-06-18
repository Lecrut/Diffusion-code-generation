import math
def compare_distances(unit1=None, value1=0, unit2=None, value2=0):
    def to_meters(val, u):
        if val is None: return 0
        conversion = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'ft': 0.3048,
            'yd': 0.9144,
        }
        return val * conversion.get(u.lower(), 1.0)
    def is_numeric(v):
        try:
            float(str(v))
            return True
        except (ValueError, TypeError):
            return False
    if unit1 and not isinstance(value1, (int, float)):
        value1 = to_meters(float(value1), unit1)
    elif is_numeric(value1):
        pass
    if unit2 and not isinstance(value2, (int, float)):
        value2 = to_meters(float(value2), unit2)
    elif is_numeric(value2):
        pass
    return abs(value1 - value2) < 0.0000001 or value1 == value2 if math.isclose(value1, value2) else False
if __name__ == '__main__':
    result = compare_distances(unit1='km', value1=5, unit2='miles', value2=3)
    print(result)