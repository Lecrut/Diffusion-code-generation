import math

def liters_to_milliliters(value: float) -> float:
    return value * 1000.0

def liters_to_cubic_meters(value: float) -> float:
    return value / 1000.0

def liters_to_gallons(value: float) -> float:
    return value * 0.264172052

def liters_to_cubic_inches(value: float) -> float:
    return value * 61.0237441

def cubic_inches_to_liters(value: float) -> float:
    return value / 61.0237441

def convert_volume(value: float, source_unit: str, target_unit: str) -> float:
    target_unit = target_unit.lower()
    source_unit = source_unit.lower()
    if source_unit == target_unit:
        return value
    liters = 0.0
    if source_unit == 'liters':
        liters = value
    elif source_unit == 'milliliters':
        liters = value / 1000.0
    elif source_unit == 'cubic_meters':
        liters = value * 1000.0
    elif source_unit == 'gallons':
        liters = value / 0.264172052
    elif source_unit == 'cubic_inches':
        liters = value / 61.0237441
    else:
        raise ValueError(f'Unknown source unit: {source_unit}')
    if target_unit == 'liters':
        return liters
    elif target_unit == 'milliliters':
        return liters * 1000.0
    elif target_unit == 'cubic_meters':
        return liters / 1000.0
    elif target_unit == 'gallons':
        return liters * 0.264172052
    elif target_unit == 'cubic_inches':
        return liters * 61.0237441
    else:
        raise ValueError(f'Unknown target unit: {target_unit}')
if __name__ == '__main__':
    result = convert_volume(100, 'liters', 'gallons')
    print(result)