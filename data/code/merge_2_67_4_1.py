import math
class TemperatureConverter:
    def to_celsius(self, kelvin):
        return kelvin - 273.15
    def to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, fahrenheit):
        return ((fahrenheit - 32) * 5 / 9) + 273.15
def convert_temperature(value: float, from_scale: str, to_scale: str) -> tuple[float, dict]:
    converter = TemperatureConverter()
    if not isinstance(value, (int, float)):
        raise TypeError("Temperature value must be a number")
    valid_scales = ['celsius', 'fahrenheit', 'kelvin']
    if from_scale not in valid_scales or to_scale not in valid_scales:
        return None, {"error": "Invalid scale"}
    try:
        celsius_value = 0.0
        intermediate_result = {}
        if from_scale == 'celsius':
            celsius_value = value
        elif from_scale == 'fahrenheit':
            temp_obj = TemperatureConverter()
            celsius_value = (value - 32) * 5 / 9
            intermediate_result['step1'] = {'from_fah_to_cel', f'{value}°F -> {celsius_value:.4f}°C'}
        elif from_scale == 'kelvin':
            temp_obj = TemperatureConverter()
            celsius_value = value - 273.15
            intermediate_result['step1'] = {'from_kel_to_cel', f'{value}K -> {celsius_value:.4f}°C'}
        if to_scale == 'celsius':
            final_temp = celsius_value
        elif to_scale == 'fahrenheit':
            temp_obj = TemperatureConverter()
            final_temp = (celsius_value * 9 / 5) + 32
            intermediate_result['step2'] = {'from_cel_to_fah', f'{final_temp:.4f}°F'}
        elif to_scale == 'kelvin':
            temp_obj = TemperatureConverter()
            final_temp = celsius_value + 273.15
            intermediate_result['step2'] = {'from_cel_to_kel', f'{final_temp:.4f}K'}
        return float(final_temp), {"success": True, "intermediate_steps": intermediate_result}
    except Exception as e:
        return None, {"error": str(e)}
if __name__ == '__main__':
    test_cases = [
        (273.15, 'kelvin', 'celsius'),
        (0, 'fahrenheit', 'celsius'),
        (-459.67, 'fahrenheit', 'kelvin'),
        (100, 'celsius', 'fahrenheit'),
        (32, 'fahrenheit', 'kelvin')
    ]
    results = []
    for value, from_s, to_s in test_cases:
        res_val, meta = convert_temperature(value, from_s, to_s)
        if isinstance(res_val, float):
            results.append((value, f"{from_s} -> {to_s}", res_val))
    print("Test Results:")
    for val, path, final in results:
        print(f"Input: {val}, Path: {path}, Output: {final}")