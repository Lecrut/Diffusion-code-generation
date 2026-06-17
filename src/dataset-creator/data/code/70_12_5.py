import math
def compare_distances(unit1=None, value1=0, unit2=None, value2=0):
    def convert_to_meters(val, u):
        if val is None: return 0
        meters = float(val)
        lower_u = str(u).lower()
        if 'km' in lower_u or 'kilometer' in lower_u:
            return meters * 1000.0
        elif 'm' in lower_u and not any(x in lower_u for x in ['mm', 'cm']):                                            
            return meters
        elif 'cm' in lower_u or 'centimeter' in lower_u:
            return meters / 100.0
        elif 'mm' in lower_u or 'millimeter' in lower_u:
            return meters / 1000.0
        return float(val)
    m1 = convert_to_meters(value1, unit1)
    m2 = convert_to_meters(value2, unit2)
    diff = abs(m1 - m2)
    if m1 > m2: return 1
    elif m2 > m1: return -1
    else: return 0
if __name__ == '__main__':
    result = compare_distances(unit1='km', value1=5, unit2='miles', value2=8)
    print(result)