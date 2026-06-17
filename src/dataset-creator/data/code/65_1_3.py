import threading
FACTORS = {
    'km': 0.001,
    'cm': 100.0,
    'mm': 1000.0,
    'inches': 39.3700787402,
}
lock = threading.Lock()
def convert_meters(meters: float) -> dict:
    result = {}
    with lock:
        for unit, factor in FACTORS.items():
            converted_value = meters * factor
            result[unit] = round(converted_value, 6)
    return result
if __name__ == '__main__':
    sample_values = [5.234, 100, -7.89]
    for val in sample_values:
        conversions = convert_meters(val)
        print(f"Input ({val} m): {conversions}")