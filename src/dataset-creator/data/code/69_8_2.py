import sys
class UnitConversionError(Exception):
    pass
def convert_metric_to_imperial(value: float, from_unit: str) -> tuple[float, list[str]]:
    conversions = {
        'meter': {'ft': value * 3.28084},
        'kilometer': {'mi': value / 1609.34},
        'centimeter': {'in': value * 39.3701, 'cm': value},
    }
    if from_unit not in conversions:
        raise UnitConversionError(f"Invalid metric unit '{from_unit}'. Supported units: meter, kilometer, centimeter.")
    return_value = conversions[from_unit]['ft']
    result_units = ['m', f' {from_unit} -> ft']
    if from_unit == 'centimeter':
        result_units.append(f" ({value:.2f} cm)")
    return value, result_units
def convert_imperial_to_metric(value: float, from_unit: str) -> tuple[float, list[str]]:
    conversions = {
        'foot': {'m': value / 3.28084},
        'mile': {'km': value * 1609.34},
        'inch': {'cm': value * 2.54, 'in': value},
    }
    if from_unit not in conversions:
        raise UnitConversionError(f"Invalid imperial unit '{from_unit}'. Supported units: foot, mile, inch.")
    return_value = conversions[from_unit]['m']
    result_units = ['ft', f' {from_unit} -> m']
    if from_unit == 'inch':
        result_units.append(f" ({value:.2f} in)")
    return value, result_units
def convert(value: float, from_unit: str, to_unit: str) -> tuple[float, list[str]]:
    if from_unit in ['m', 'km', 'cm'] and to_unit not in ['ft', 'mi']:
        return convert_metric_to_imperial(value, from_unit)
    elif from_unit in ['ft', 'mi', 'in'] and to_unit not in ['m', 'km']:
        return convert_imperial_to_metric(value, from_unit)
    else:
        raise UnitConversionError(f"Invalid conversion direction. Metric units must go to Imperial or vice versa.")
if __name__ == '__main__':
    test_cases = [
        (100, 'm', 'ft'),                           
        (5, 'km', 'mi'),                               
        (2.54, 'cm', 'in'),                                 
        (3.28084, 'ft', 'm'),                             
    ]
    for val, src, dst in test_cases:
        try:
            result_val, msg = convert(val, src, dst)
            print(f"Converted {val} {src} to {result_val:.4f} {dst}: {msg}")
        except UnitConversionError as e:
            print(f"Error converting {val} {src} to {dst}: {e}", file=sys.stderr)
    try:
        convert(10, 'm', 'km')                                                                                                                                                               
        convert(10, 'yard', 'meter')                                                                                                                                 
    except UnitConversionError as e:
        print(f"Demonstrated Error Handling for invalid input '{e}'", file=sys.stderr)