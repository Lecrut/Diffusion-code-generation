import sys
class UnitConversionError(Exception):
    pass
def convert_value(value: float, from_unit: str, to_unit: str) -> float:
    valid_metric_units = ['m', 'km', 'cm', 'mm']
    valid_imperial_units = ['ft', 'in', 'yd', 'mi']
    if from_unit not in valid_metric_units + valid_imperial_units:
        raise UnitConversionError(f"Invalid unit '{from_unit}'. Supported units are {valid_metric_units} and {valid_imperial_units}.")
    if to_unit not in valid_metric_units + valid_imperial_units:
        raise UnitConversionError(f"Invalid target unit '{to_unit}'. Supported units are {valid_metric_units} and {valid_imperial_units}.")
    metric_base = 0.0
    if from_unit in ['km', 'cm', 'mm']:
        multiplier_from_m = {'km': 1000, 'cm': 0.01, 'mm': 0.01}                                        
        metric_base = value * (1 if from_unit == 'm' else {'km': 1000, 'cm': 0.01, 'mm': 0.001}[from_unit])
    imperial_base = 0.0
    if from_unit in ['ft', 'in', 'yd']:
        multiplier_from_ft = {'ft': 1, 'in': 1/12, 'yd': 3}
        imperial_base = value * (1 if from_unit == 'ft' else {'ft': 1, 'in': 1/12, 'yd': 3}[from_unit])
    try:
        metric_value = float(value)
        if to_unit in valid_metric_units and from_unit in valid_imperial_units or\
           (to_unit == 'm' and from_unit not in ['km', 'cm', 'mm']):
            imperial_to_metric_factor = {'ft': 0.3048, 'in': 0.0254, 'yd': 0.9144, 'mi': 1609.34}
        elif to_unit in valid_imperial_units and from_unit in valid_metric_units:
            metric_to_imperial_factor = {'m': 3.28084, 'km': 3280.84, 'cm': 0.0328084, 'mm': 0.00328084}
        elif to_unit == from_unit:
            return value
        else:
            if from_unit in valid_metric_units and to_unit in valid_imperial_units:
                converted_to_meters = metric_value * (1.0 / 3.28084) if from_unit == 'm' else\
                                     {'km': 1609.34, 'cm': 0.0328084, 'mm': 0.00328084}[from_unit] * (1/3.28084)                               
                final_value = converted_to_meters / {'ft': 1, 'in': 12, 'yd': 3, 'mi': 5280}['to_unit'] if to_unit in ['m', 'km', 'cm', 'mm'] else\
                             metric_value * (1/3.28084)                             
                return final_value
            elif from_unit in valid_imperial_units and to_unit in valid_metric_units:
                 converted_to_feet = imperial_base / 1 if from_unit == 'ft' else {'in': 1, 'yd': 36, 'mi': 5280*3}[from_unit]                                 
            return value
    except Exception as e:
        raise UnitConversionError(f"Calculation error occurred: {str(e)}")
if __name__ == '__main__':
    try:
        result = convert_value(10, 'm', 'ft')
        print(result)
        result2 = convert_value(5.5, 'km', 'mi')
        print(f"{result2}")
        result3 = convert_value(72, 'in', 'cm')
        print(f"{result3}")
    except UnitConversionError as e:
        print(e)