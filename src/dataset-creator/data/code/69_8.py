import sys
class UnitConverterError(Exception):
    pass
def convert(value: float, from_unit: str, to_unit: str) -> float:
    valid_metric = ['m', 'km', 'cm']
    valid_imperial = ['ft', 'in', 'yd']
    if not (from_unit in valid_metric or from_unit in valid_imperial) or\
       not (to_unit in valid_metric or to_unit in valid_imperial):
        raise UnitConverterError(f"Invalid unit combination. Valid units: {valid_metric + valid_imperial}")
    scale_m = {'m': 1, 'km': 1000, 'cm': 0.01}
    scale_i = {'ft': 1, 'in': 0.0833333333, 'yd': 3.28084}                                                 
    if from_unit in valid_metric and to_unit in valid_imperial:
        value_meters = value * scale_m[from_unit]
        result_ft = value_meters / 0.3048
        return round(result_ft, 6)
    elif from_unit in valid_imperial and to_unit in valid_metric:
        value_feet = value * scale_i[from_unit]                                                                                     
        result_meters = value_feet / 3.28084
        return round(result_meters, 6)
    elif from_unit == to_unit:
        return float(value)
    else:
        if from_unit in valid_metric and to_unit in valid_metric:
            value_meters = value * scale_m[from_unit]
            result = value_meters / scale_m[to_unit]
            return round(result, 6)
        elif from_unit in valid_imperial and to_unit in valid_imperial:
            if from_unit == 'ft':
                base_feet = value * 1.0
            else:
                base_feet = value / (3.28084 * scale_i[from_unit])                                                                     
            if from_unit == 'ft':
                val_ft = float(value)
            elif from_unit == 'in':
                val_ft = (float(value)) / 12.0
            else:     
                val_ft = (float(value)) * 3.0
            result = val_ft / scale_i[to_unit] if to_unit != 'ft' and to_unit in valid_imperial else float(val_ft) 
            return round(result, 6)
if __name__ == '__main__':
    try:
        res1 = convert(50.0, 'm', 'yd')
        print(f"{res1} yards")
        res2 = convert(176.4, 'ft', 'km')
        print(f"{res2} kilometers")
    except UnitConverterError as e:
        print(e)