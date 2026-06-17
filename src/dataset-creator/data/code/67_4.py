import math
class TemperatureConverter:
    def to_celsius(self, temperature_fahrenheit):
        return (temperature_fahrenheit - 32) * 5 / 9
    def to_fahrenheit(self, temperature_celsius):
        return (temperature_celsius * 9 / 5) + 32
    def to_kelvin(self, temperature_celsius):
        return temperature_celsius + 273.15
    def to_celsius_from_kelvin(self, temperature_kelvin):
        return temperature_kelvin - 273.15
def convert_temperature(value: float, from_scale: str, to_scale: str) -> dict:
    converter = TemperatureConverter()
    scale_map = {
        'F': ('fahrenheit', lambda x: (x - 32) * 5 / 9),
        'C': ('celsius', None),
        'K': ('kelvin', lambda x: x - 273.15)
    }
    if from_scale not in scale_map or to_scale not in scale_map:
        raise ValueError(f"Invalid temperature scale. Supported scales: {list(scale_map.keys())}")
    source_func = None
    target_celsius = False
    if from_scale == 'C':
        result = converter.to_kelvin(value) if to_scale == 'K' else value
        return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': result}
    elif from_scale == 'F':
        celsius_val = (value - 32) * 5 / 9
        if to_scale == 'C':
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': celsius_val}
        elif to_scale == 'K':
            result = converter.to_kelvin(celsius_val)
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': result}
    else:               
        celsius_val = temperature_kelvin - 273.15
        if to_scale == 'C':
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': celsius_val}
        elif to_scale == 'F':
            result = (celsius_val * 9 / 5) + 32
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': result}
def run_tests():
    test_cases = [
        (-40.0, 'F', -40.0),
        (32.0, 'F', 0.0),
        (186.579, 'C', 273.15),
        (273.15, 'K', 0.0),
    ]
    passed = 0
    for temp_in, unit_in, expected_out in test_cases:
        try:
            result = convert_temperature(temp_in, unit_in[0], unit_in[1])
            if abs(result['converted_value'] - expected_out) < 0.001:
                passed += 1
            else:
                print(f"Test failed for {temp_in}°{unit_in[2]} -> Expected ~{expected_out}, Got {result['converted_value']}")
        except Exception as e:
            print(f"Exception during test conversion of {temp_in}: {e}")
if __name__ == '__main__':
    run_tests()