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
    def get_value():
        if isinstance(value1, (int, float)) and value2 is None:
            return abs(float(value1) - float(value2))
        meters1 = to_meters(value1, unit1) if unit1 else float(value1)
        meters2 = to_meters(value2, unit2) if unit2 else float(value2)
        diff = abs(meters1 - meters2)
        return diff
    result = get_value()
    val1_raw = value1 if isinstance(value1, (int, float)) else None
    val2_raw = value2 if isinstance(value2, (int, float)) else None
    if unit1 and not unit2:
        meters1 = to_meters(val1_raw, unit1)
        return f"{meters1} m"
    elif unit2 and not unit1:
        meters2 = to_meters(val2_raw, unit2)
        return f"{meters2} m"
def main():
    print(compare_distances(unit1='km', value1=5))
    print(compare_distances(value1=10.5, value2=3.7))
    print(compare_distances(unit1='mi', value1=2, unit2='ft', value2=6000))
if __name__ == '__main__':
    main()