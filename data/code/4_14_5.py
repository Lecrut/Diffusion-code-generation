def convert_distance(value, source_unit, target_unit):
    METER_TO_FEET = 3.28084
    METER_TO_MILE = 0.000621371
    METER_TO_KM = 0.001
    FEET_TO_METER = 1 / METER_TO_FEET
    MILE_TO_METER = 1 / METER_TO_MILE
    KM_TO_METER = 1 / METER_TO_KM

    valid_units = {'m', 'km', 'mi', 'ft'}
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError("Value must be a numeric type")
    if source_unit.lower() not in valid_units:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_unit.lower() not in valid_units:
        raise ValueError(f"Invalid target unit: {target_unit}")

    value_str = str(value).lower().strip()
    source_str = str(source_unit).lower().strip()
    target_str = str(target_unit).lower().strip()

    if source_str == 'm':
        meters = value
    elif source_str == 'km':
        meters = value * KM_TO_METER
    elif source_str == 'mi':
        meters = value * MILE_TO_METER
    elif source_str == 'ft':
        meters = value * FEET_TO_METER

    if target_str == 'm':
        result = meters
    elif target_str == 'km':
        result = meters * METER_TO_KM
    elif target_str == 'mi':
        result = meters * METER_TO_MILE
    elif target_str == 'ft':
        result = meters * METER_TO_FEET

    return round(result, 6)

if __name__ == '__main__':
    print(convert_distance(100, 'm', 'ft'))
    print(convert_distance(1, 'km', 'mi'))
    print(convert_distance(5280, 'ft', 'mi'))
    print(convert_distance(10, 'mi', 'km'))