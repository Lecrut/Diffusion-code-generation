import re
class TemperatureValidator:
    def is_numeric(self, value):
        if isinstance(value, (int, float)):
            return True
        try:
            float(str(value))
            return True
        except ValueError:
            return False
def convert_temperature(temp_value, from_scale, to_scale):
    validator = TemperatureValidator()
    if not validator.is_numeric(temp_value) or temp_value is None:
        raise TypeError("Input temperature must be a numeric value.")
    valid_scales = ["celsius", "fahrenheit", "kelvin", "rankine"]
    from_lower = from_scale.lower().strip()
    to_lower = to_scale.lower().strip()
    if not (from_lower in valid_scales and to_lower in valid_scales):
        raise ValueError(f"Invalid scale. Must be one of: {', '.join(valid_scales)}")
    celsius_temp = None
    try:
        temp_float = float(temp_value)
    except ValueError:
        raise TypeError("Temperature value must be convertible to a float.")
    if from_lower == "celsius":
        celsius_temp = temp_float
    elif from_lower == "fahrenheit":
        celsius_temp = (temp_float - 32) * 5 / 9
    elif from_lower == "kelvin":
        celsius_temp = temp_float - 273.15
    elif from_lower == "rankine":
        celsius_temp = (temp_float - 491.67) * 5 / 9
    if to_scale.lower() in ["celsius", "fahrenheit"]:
        return round(celsius_temp, 2), f"{to_scale} temperature"
    elif to_scale.lower() == "kelvin":
        kelvin = celsius_temp + 273.15
        return round(kelvin, 4), f"{to_scale} temperature"
    else:          
        rankine = (celsius_temp * 9 / 5) + 491.67
        return round(rankine, 2), f"{to_scale} temperature"
if __name__ == '__main__':
    test_cases = [
        ("fahrenheit", "kelvin", 32),
        ("celsius", "rankine", 0),
        ("invalid_input", "celsius", None)                                                                                                                                                                                                                                                                                                                                                                         
    ]
    print("Running Temperature Conversion Utility...")
    try:
        result = convert_temperature(32.0, "fahrenheit", "kelvin")
        print(f"Input: 32 F -> Output: {result[1]} ({result[0]}) K")
        try:
            result = convert_temperature("abc", "celsius", "fahrenheit")
        except TypeError as e:
            print(f"Caught expected error for invalid numeric input 'abc': {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")