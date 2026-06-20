def convert_length(length: float, unit: str) -> float:
    unit = unit.lower()
    if unit in ('m', 'meter', 'meters'):
        return length
    elif unit in ('ft', 'foot', 'feet'):
        return length * 0.3048
    elif unit in ('cm', 'centimeter', 'centimeters'):
        return length / 100.0
    elif unit in ('mm', 'millimeter', 'millimeters'):
        return length / 1000.0
    elif unit in ('km', 'kilometer', 'kilometers'):
        return length * 1000.0
    elif unit in ('in', 'inch', 'inches'):
        return length * 0.0254
    elif unit in ('yd', 'yard', 'yards'):
        return length * 0.9144
    elif unit in ('mi', 'mile', 'miles'):
        return length * 1609.344
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    result = convert_length(100, 'ft')
    print(result)