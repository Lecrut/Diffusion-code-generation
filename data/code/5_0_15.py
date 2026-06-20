import re

def calculate_length_difference(first_measurement: str, second_measurement: str) -> float:
    first_value = parse_length_measurement(first_measurement)
    second_value = parse_length_measurement(second_measurement)
    if first_value is None or second_value is None:
        raise ValueError('Invalid length measurement provided.')
    return first_value - second_value

def parse_length_measurement(measurement: str) -> float:
    if measurement is None or not isinstance(measurement, str):
        return None
    measurement = measurement.strip()
    if not measurement:
        return None
    if not re.match('^[+-]?(\\d+\\.?\\d*|\\.\\d+)$', measurement):
        return None
    return float(measurement)
if __name__ == '__main__':
    first_input = '10.5 cm'
    second_input = '5.2 cm'
    try:
        result = calculate_length_difference(first_input, second_input)
        print(result)
    except ValueError as e:
        print(str(e))