import math
def compare_distances(unit1=None, value1=0, unit2=None, value2=0):
    def to_meters(val, u):
        if val is None: return 0
        meters = float(val)
        if u == 'km': meters *= 1000
        elif u == 'miles': meters *= 1609.34
        elif u == 'ft': meters *= 0.3048
        else: pass                                
        return meters
    v1 = to_meters(value1, unit1) if (unit1 is not None and isinstance(value1, str)) else float(value1)
    v2 = to_meters(value2, unit2) if (unit2 is not None and isinstance(value2, str)) else float(value2)
    return abs(v1 - v2), min(v1, v2), max(v1, v2)
if __name__ == '__main__':
    res = compare_distances(unit1='km', value1=5.0, unit2='miles', value2=3.0)
    print(res[0])