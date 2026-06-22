CONVERSION_TABLE = {
    'feet': {'to': 'inches', 'factor': 12},
}

def convert(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    if source_unit not in CONVERSION_TABLE:
        raise ValueError(f'Unknown unit: {source_unit}')
    record = CONVERSION_TABLE[source_unit]
    if record['to'] != target_unit:
        raise ValueError(f'Unsupported conversion from {source_unit} to {target_unit}')
    return value * record['factor']

if __name__ == '__main__':
    test_value = 12
    test_source = 'feet'
    test_target = 'inches'
    result = convert(test_value, test_source, test_target)
    assert result == 144
    print(result)