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
            if 'mm' in unit or 'cm' in unit:
                rounded_val = round(converted_value, 2)
            else:
                rounded_val = round(converted_value, 6)
            result[unit] = rounded_val
    return result
if __name__ == '__main__':
    sample_values = [1.5, -0.75, 3000]
    for val in sample_values:
        conversions = convert_meters(val)
        print(f"Input ({val} m):")
        for unit, converted_val in conversions.items():
            print(f"{unit}: {converted_val}")