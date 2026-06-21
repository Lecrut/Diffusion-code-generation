class LengthConversionError(Exception):
    def __init__(self, message, context):
        self.context = context
        super().__init__(message)

class UnsupportedUnitError(LengthConversionError):
    def __init__(self, unit):
        context = {"unit": unit}
        super().__init__(f"Unsupported unit: {unit}", context)

class InvalidValueError(LengthConversionError):
    def __init__(self, value):
        context = {"value": value}
        super().__init__(f"Invalid value: {value}", context)

class ZeroValueError(LengthConversionError):
    def __init__(self, value):
        context = {"value": value}
        super().__init__(f"Zero value is not allowed: {value}", context)

CONVERSION_FACTORS = {
    "meters": 1.0,
    "feet": 0.3048,
    "inches": 0.0254,
    "yards": 0.9144,
    "kilometers": 1000.0,
    "centimeters": 0.01,
}

def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise InvalidValueError(value)
    if value < 0:
        raise InvalidValueError(value)
    if value == 0:
        raise ZeroValueError(value)
    if from_unit not in CONVERSION_FACTORS:
        raise UnsupportedUnitError(from_unit)
    if to_unit not in CONVERSION_FACTORS:
        raise UnsupportedUnitError(to_unit)
    meters = value * CONVERSION_FACTORS[from_unit]
    converted = meters / CONVERSION_FACTORS[to_unit]
    return converted

if __name__ == '__main__':
    result = convert_length(10, 'feet', 'meters')
    print(result)
    result2 = convert_length(100, 'centimeters', 'inches')
    print(result2)
    result3 = convert_length(5.5, 'kilometers', 'miles')
    print(result3)
    try:
        convert_length(10, 'feet', 'lightyears')
    except UnsupportedUnitError as e:
        print(e.context)
    try:
        convert_length(-5, 'meters', 'feet')
    except InvalidValueError as e:
        print(e.context)
    try:
        convert_length(0, 'meters', 'feet')
    except ZeroValueError as e:
        print(e.context)
    try:
        convert_length("ten", 'meters', 'feet')
    except InvalidValueError as e:
        print(e.context)
    result4 = convert_length(1, 'meter', 'foot')
    print(result4)
    result5 = convert_length(12, 'inches', 'feet')
    print(result5)
    result6 = convert_length(3, 'yards', 'feet')
    print(result6)