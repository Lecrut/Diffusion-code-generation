import math
class UnitConverterError(Exception):
    pass
def convert_value(value: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
    metric_units = {
        'm': {'name': 'meter', 'factor': 1.0},
        'km': {'name': 'kilometer', 'factor': 1e3},
        'cm': {'name': 'centimeter', 'factor': 1e-2},
        'mm': {'name': 'millimeter', 'factor': 1e-3}
    }
    imperial_units = {
        'ft': {'name': 'foot', 'factor_to_meter': 0.3048, 'inverse_factor': 1/0.3048},
        'in': {'name': 'inch', 'factor_to_meter': 0.0254, 'inverse_factor': 1/0.0254}
    }
    if from_unit not in metric_units and from_unit not in imperial_units:
        raise UnitConverterError(f"Invalid unit '{from_unit}'. Supported metric: {list(metric_units.keys())}, Imperial: {list(imperial_units.keys())}")
    if to_unit not in metric_units and to_unit not in imperial_units:
        raise UnitConverterError(f"Invalid target unit '{to_unit}'. Supported metric: {list(metric_units.keys())}, Imperial: {list(imperial_units.keys())}")
    from_scale = 'metric' if from_unit in metric_units else 'imperial'
    to_scale = 'metric' if to_unit in metric_units else 'imperial'
    if from_scale != to_scale:
        raise UnitConverterError("Cannot convert between different scales (e.g., meter to foot). Use a common intermediate unit.")
    try:
        converted_value = 0.0
        if from_scale == 'metric':
            base_meters = value * metric_units[from_unit]['factor']
            if to_unit in metric_units:
                final_result = base_meters / metric_units[to_unit]['factor']
            else:                      
                final_result = base_meters * imperial_units[to_unit]['inverse_factor']
        elif from_scale == 'imperial':
            if from_unit in imperial_units:
                base_meters = value / imperial_units[from_unit]['factor_to_meter']
                if to_unit in metric_units:
                    final_result = base_meters * metric_units[to_unit]['factor']
                else:                                   
                    factor_imperial_ratio = imperial_units[to_unit]['inverse_factor'] / imperial_units[from_unit]['factor_to_meter']
                    final_result = value * factor_imperial_ratio
            else: 
                raise UnitConverterError(f"Invalid source unit '{from_unit}' for Imperial conversion.")
        return round(final_result, 4), {
            'original_value': value,
            'source_unit': from_unit,
            'target_unit': to_unit,
            'conversion_factor_approx': final_result / (value if abs(value) > 0 else 1)
        }
    except Exception as e:
        raise UnitConverterError(f"Conversion failed due to internal error: {str(e)}")
if __name__ == '__main__':
    try:
        result, info = convert_value(10.5, 'km', 'm')
        print(f"{info['original_value']} km -> {result} m (Factor: ~{info['conversion_factor_approx']})")
        result2, _ = convert_value(34867.9, 'ft', 'in')
        print(f"Conversion from feet to inches completed successfully.")
    except UnitConverterError as e:
        print(f"Handled error gracefully: {e}")