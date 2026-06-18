import re
def parse_volume_strings(strings):
    mapping = {
        'L': 1,
        'l': 1,
        'm³': 0.001,
        'cm³': 0.000001,
        'mm³': 0.000000001,
    }
    def convert(value):
        if isinstance(value, float):
            return value
        match = re.match(r'^([+-]?[\d\.]+)\s*(L|l|m³|cm³|mm³)?$', str(value).strip())
        if not match:
            raise ValueError(f"Invalid volume string: {value}")
        amount = float(match.group(1))
        unit = match.group(2) or 'L'
        factor = mapping.get(unit, 1.0)
        return amount * factor
    result = [convert(s) for s in strings]
    return result
if __name__ == '__main__':
    test_data = ['5 L', '-3 m³', '2cm³', 4.5, 'invalid']
    try:
        output = parse_volume_strings(test_data)
        print(output)
    except ValueError as e:
        print(e)