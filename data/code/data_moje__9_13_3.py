from __future__ import annotations

from typing import Union

MetricUnit = Union[float, int]
ImperialUnit = Union[float, int]

def convert_metric_to_imperial(
    value: float,
    unit: str
) -> float:
    if unit == 'L':
        return value * 0.264172
    if unit == 'mL':
        return (value / 1000.0) * 0.264172
    if unit == 'm³':
        return value * 264.172
    raise ValueError(f"Unsupported metric unit: {unit}")

def convert_imperial_to_metric(
    value: float,
    unit: str
) -> float:
    if unit == 'L':
        return value / 0.264172
    if unit == 'gal':
        return value / 0.264172
    raise ValueError(f"Unsupported imperial unit: {unit}")

def convert_volume(
    value: float,
    from_unit: str,
    to_unit: str
) -> float:
    if from_unit == to_unit:
        return value
    
    metric_units = {'L', 'mL', 'm³'}
    imperial_units = {'gal'}
    
    if from_unit not in metric_units and from_unit not in imperial_units:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in metric_units and to_unit not in imperial_units:
        raise ValueError(f"Unknown target unit: {to_unit}")
    
    if from_unit in metric_units and to_unit in imperial_units:
        intermediate = convert_metric_to_imperial(value, from_unit)
        return intermediate
    if from_unit in imperial_units and to_unit in metric_units:
        intermediate = convert_imperial_to_metric(value, from_unit)
        return intermediate
    
    return value

if __name__ == '__main__':
    liters = 5.0
    gallons = convert_volume(liters, 'L', 'gal')
    print(gallons)
    
    gallons_input = 2.5
    liters_out = convert_volume(gallons_input, 'gal', 'L')
    print(liters_out)
    
    milliliters = 1000.0
    cubic_meters = convert_volume(milliliters, 'mL', 'm³')
    print(cubic_meters)