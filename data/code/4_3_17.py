def _to_metric(value, metric_unit):
    conversions = {
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34,
        'pound': 0.453592,
        'ounce': 0.0283495,
        'gallon': 3.78541,
    }
    if metric_unit in conversions:
        return value * conversions[metric_unit]
    raise ValueError(f"Unsupported imperial unit: {metric_unit}")

def _from_metric(value, metric_unit):
    inv_conversions = {
        'meter': 1 / 0.0254,
        'meter': 1 / 0.3048,
        'meter': 1 / 0.9144,
        'meter': 1 / 1609.34,
        'kilogram': 1 / 0.453592,
        'kilogram': 1 / 0.0283495,
        'liter': 1 / 3.78541,
    }
    if metric_unit == 'meter':
        return value / 0.0254
    if metric_unit == 'kilogram':
        return value / 0.453592
    if metric_unit == 'liter':
        return value / 3.78541
    if metric_unit == 'mile':
        return value / 1609.34
    if metric_unit == 'foot':
        return value / 0.3048
    if metric_unit == 'yard':
        return value / 0.9144
    if metric_unit == 'ounce':
        return value / 0.0283495
    if metric_unit == 'pound':
        return value / 0.453592
    if metric_unit == 'gallon':
        return value / 3.78541
    raise ValueError(f"Unsupported metric unit: {metric_unit}")

def convert(value, from_unit, to_unit):
    metric_map = {
        'inch': 'meter', 'foot': 'meter', 'yard': 'meter', 'mile': 'meter',
        'pound': 'kilogram', 'ounce': 'kilogram',
        'gallon': 'liter',
    }
    imperial_map = {
        'meter': 'foot', 'kilogram': 'pound', 'liter': 'gallon',
    }
    if from_unit == to_unit:
        return value
    if from_unit not in metric_map:
        raise ValueError(f"Unsupported imperial unit: {from_unit}")
    if to_unit not in imperial_map:
        raise ValueError(f"Unsupported imperial unit: {to_unit}")
    metric_value = value * metric_map[from_unit]
    if from_unit in metric_map and metric_map[from_unit] == 'meter':
        if to_unit == 'foot':
            return metric_value / 0.3048
        if to_unit == 'yard':
            return metric_value / 0.9144
        if to_unit == 'mile':
            return metric_value / 1609.34
        if to_unit == 'inch':
            return metric_value / 0.0254
    if from_unit in metric_map and metric_map[from_unit] == 'kilogram':
        if to_unit == 'pound':
            return metric_value / 0.453592
        if to_unit == 'ounce':
            return metric_value / 0.0283495
    if from_unit in metric_map and metric_map[from_unit] == 'liter':
        if to_unit == 'gallon':
            return metric_value / 3.78541
    raise ValueError(f"Conversion between {from_unit} and {to_unit} not supported")

if __name__ == '__main__':
    result_inches = convert(1, 'foot', 'inch')
    print(result_inches)
    result_kg = convert(1, 'pound', 'kilogram')
    print(result_kg)
    result_liters = convert(1, 'gallon', 'liter')
    print(result_liters)
    result_meters = convert(1, 'mile', 'meter')
    print(result_meters)