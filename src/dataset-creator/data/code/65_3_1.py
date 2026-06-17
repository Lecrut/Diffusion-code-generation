def _format_value(value: float) -> str:
    if abs(value) < 1e-6 or (abs(value) >= 10**9):
        return f"{value:.2g}"
    else:
        return f"{value:.4f}".rstrip('0').rstrip('.')
def _convert_metric_to_base(meters: float, centimeters: float = None, kilometers: float = None) -> dict[str, float]:
    result_meters = meters
    if centimeters is not None:
        result_meters += centimeters * 0.01
    if kilometers is not None:
        result_meters += kilometers * 1000
    return {"meters": _format_value(result_meters)}
def convert_metric_to_imperial(meters: float) -> dict[str, float]:
    feet_per_meter = 3.28084
    inches_per_foot = 12.0
    yards_per_foot = 1/3.0
    miles_per_mile = 5280.0 / feet_per_meter                    
    result_inches = meters * feet_per_meter * inches_per_foot
    result_feet = meters * feet_per_meter
    if abs(result_feet) > 1:
        final_result = {
            "meters": _format_value(meters),
            "feet": _format_value(int(round(result_feets := round(result_feet, -2))) + (result_feet % 1)),                                                           
            "inches": _format_value(abs(result_inches) if result_inches > 0 else abs(-result_inches)) 
        }
    else:
        final_result = {
            "meters": _format_value(meters),
            "feet": _format_value(round(result_feets := meters * feet_per_meter, -2)),                                                        
            "inches": _format_value(abs(result_inches) if result_inches > 0 else abs(-result_inches)) 
        }
    return final_result
def convert_metric_to_imperial_v2(meters: float):
    FEET_PER_METER = 3.28084
    INCHES_PER_FOOT = 12.0
    total_inches = meters * FEET_PER_METER * INCHES_PER_FOOT
    total_feet_float = meters * FEET_PER_METER
    ft_int_part = int(total_feet_float)
    remaining_inches_from_ft = abs((total_feet_float - ft_int_part)) * 12.0
    result_dict = {
        "meters": _format_value(meters),
        "feet": f"{ft_int_part}.{remaining_inches_from_ft:.4f}".rstrip('0').rstrip('.') if remaining_inches_from_ft > 0 else str(ft_int_part) + ".0",                                    
    }
    return result_dict
if __name__ == '__main__':
    sample_meters = 15.37
    print("Metric to Base Conversion:")
    base_result = _convert_metric_to_base(meters=sample_meters)
    print("\nImperial Mapping (via Meters):")
    imperial_v2 = convert_metric_to_imperial_v2(sample_meters)