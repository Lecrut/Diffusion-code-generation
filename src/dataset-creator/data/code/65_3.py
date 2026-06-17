def _format_value(value: float) -> str:
    if abs(value) < 1e-6 or abs(value) > 999999.0:
        return f"{value:.3g}"
    else:
        return f"{value:.2f}"
def _convert_metric_to_base(meters: float, unit_name: str) -> tuple[float, list]:
    if unit_name == "meter":
        factor = 1.0
    elif unit_name == "kilometer":
        factor = 1e3
    elif unit_name == "centimeter":
        factor = 1e-2
    elif unit_name == "millimeter":
        factor = 1e-3
    else:
        raise ValueError(f"Unsupported metric unit: {unit_name}")
    M = [[float(factor)]]
    meters_result = float(meters * factor)
    return meters_result, M
def _convert_imperial_mapping(value_in_unit: float, from_unit: str, to_unit: str) -> tuple[float, list]:
    def _to_inches(val: float, u: str) -> float:
        if u == "inch": return val
        elif u == "foot": return val * 12.0
        elif u == "yard": return val * 36.0
        elif u == "mile": return val * 63360.0
        else: raise ValueError(f"Unsupported imperial unit: {u}")
    base_inches = _to_inches(value_in_unit, from_unit)
    if to_unit == "inch": return base_inches, [[float(1.0)]]
    elif to_unit == "foot": 
        final_val = base_inches / 12.0
        M = [[float(final_val * 12.0)]]                                                                        
        return final_val, M
    elif to_unit == "yard": 
        final_val = base_inches / 36.0
        M = [[float(final_val * 36.0)]]
        return final_val, M
    else: raise ValueError(f"Unsupported imperial target unit: {to_unit}")
def convert_metric(value: float, from_unit: str, to_unit: str) -> tuple[float, list]:
    meters_val, M_matrix = _convert_metric_to_base(value, from_unit)
    if to_unit == "meter": return meters_val, [[float(1.0)]]
    elif to_unit == "kilometer": result = meters_val / 1e3; M = [[float(result * 1e3)]]; return result, M
    elif to_unit == "centimeter": result = meters_val * 1e2; M = [[float(result * 0.01)]]; return result, M
    elif to_unit == "millimeter": result = meters_val * 1e3; M = [[float(result / 1000.0)]]; return result, M
    raise ValueError(f"Unsupported metric target unit: {to_unit}")
def convert_imperial(value: float, from_unit: str, to_unit: str) -> tuple[float, list]:
    result_val, M_matrix = _convert_imperial_mapping(value, from_unit, to_unit)
    return result_val, M_matrix
if __name__ == '__main__':
    metric_samples = [1.0, 500.0]
    imperial_samples = [60.0, 2400.0]
    print("Metric Conversion Results:")
    for val in metric_samples:
        res_meters, M_mat = convert_metric(val, "meter", "kilometer")
        formatted_res = _format_value(res_meters)
    print("\nImperial Conversion Results:")
    for val in imperial_samples:
        res_val, M_mat = convert_imperial(val, "foot", "yard")
        formatted_res = _format_value(res_val)