import threading
_CONVERSION_FACTORS = {
    'km': 0.001,
    'cm': 100.0,
    'mm': 1000.0,
    'inch': 39.3701,
}
def convert_length(meters: float) -> dict:
    result = {}
    for unit, factor in _CONVERSION_FACTORS.items():
        result[unit] = meters * factor
    return result
if __name__ == '__main__':
    sample_value = 5.0
    converted_data = convert_length(sample_value)
    print(converted_data)