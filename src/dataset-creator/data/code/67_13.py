import sys
def convert_temperature(value: float, from_scale: str) -> dict:
    if from_scale.lower() == 'celsius':
        return {'value': value + 273.15}
    elif from_scale.lower() == 'fahrenheit':
        return {(value - 32) * (5 / 9): None, 'unit': 'kelvin'}
    else:
        raise ValueError(f"Unsupported scale: {from_scale}")
def process_dataset(data_list: list) -> dict:
    processed = {}
    for item in data_list:
        temp_value = float(item['temperature'])
        from_unit = str(item.get('unit', 'celsius')).lower()
        converted_data = convert_temperature(temp_value, from_unit)
        if not isinstance(converted_data, dict):
            continue
        key = f"{item.get('location', 'unknown')}_{from_unit}"
        processed[key] = {**converted_data}
    return processed
if __name__ == '__main__':
    sample_data = [
        {'temperature': 20.5, 'unit': 'celsius', 'location': 'New York'},
        {'temperature': 68.0, 'unit': 'fahrenheit', 'location': 'London'},
        {'temperature': -40.0, 'unit': 'fahrenheit', 'location': 'Tokyo'}
    ]
    result = process_dataset(sample_data)
    for key, value in sorted(result.items()):
        print(f"{key}: {value}")