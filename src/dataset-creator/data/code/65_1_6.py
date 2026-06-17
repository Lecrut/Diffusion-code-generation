import threading
FACTORS = {
    'km': 0.001,
    'cm': 100.0,
    'mm': 1000.0,
    'inch': 39.3701,
}
lock = threading.Lock()
def convert_meters(meters: float) -> dict:
    result = {}
    with lock:
        for unit, factor in FACTORS.items():
            converted_value = meters * factor
            if isinstance(converted_value, float):
                rounded_value = round(converted_value, 6)
            else:
                rounded_value = int(converted_value)
            result[unit] = rounded_value
    return result
if __name__ == '__main__':
    sample_values = [1.5, -0.25, 3000]
    for val in sample_values:
        conversions = convert_meters(val)
        print(f"Input ({val} m): {conversions}")