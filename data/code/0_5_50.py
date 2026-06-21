def convert_length(value, from_unit, to_unit):
    METER_TO_CM = 100
    METER_TO_MM = 1000
    METER_TO_KM = 0.001
    INCH_TO_METER = 0.0254
    FOOT_TO_METER = 0.3048
    YARD_TO_METER = 0.9144
    MILE_TO_METER = 1609.34
    conversion_factors = {'m': 1, 'cm': 1 / METER_TO_CM, 'mm': 1 / METER_TO_MM, 'km': METER_TO_KM, 'in': INCH_TO_METER, 'ft': FOOT_TO_METER, 'yd': YARD_TO_METER, 'mi': MILE_TO_METER}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Unsupported unit')
    value_in_meters = value * conversion_factors[from_unit]
    converted_value = value_in_meters / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    length_value = 500
    from_unit = 'mm'
    to_unit = 'km'
    result = convert_length(length_value, from_unit, to_unit)
    print(result)