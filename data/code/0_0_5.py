def convert_length(value: float, unit: str) -> float:
    unit = unit.lower()
    if unit == 'm' or unit == 'meter' or unit == 'meters':
        return value
    if unit == 'ft' or unit == 'foot' or unit == 'feet':
        return value * 0.3048
    if unit == 'in' or unit == 'inch' or unit == 'inches':
        return value * 0.0254
    if unit == 'yd' or unit == 'yard' or unit == 'yards':
        return value * 0.9144
    if unit == 'km' or unit == 'kilometer' or unit == 'kilometers':
        return value * 1000.0
    if unit == 'mi' or unit == 'mile' or unit == 'miles':
        return value * 1609.34
    if unit == 'cm' or unit == 'centimeter' or unit == 'centimeters':
        return value * 0.01
    if unit == 'mm' or unit == 'millimeter' or unit == 'millimeters':
        return value * 0.001
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_length(10.0, 'ft'))
    print(convert_length(5.5, 'm'))
    print(convert_length(1.0, 'mi'))
    print(convert_length(100.0, 'cm'))