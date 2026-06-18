class TemperatureConverter:
    def to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9/5) + 32
    def to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def to_celsius(self, fahrenheit_or_kelvin, is_kelvin=False):
        try:
            value = int(fahrenheit_or_kelvin) if isinstance(fahrenheit_or_kelvin, str) else float(fahrenheit_or_kelvin)
            if not isinstance(value, (int, float)):
                raise ValueError("Input must be a number.")
            if is_kelvin:
                return value - 273.15
            else:
                return (value - 32) * 5/9
        except Exception as e:
            raise ValueError(f"Invalid input provided: {e}")
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_samples = [0, 100, -40]
    print("Celsius -> Fahrenheit:", end=" ")
    for temp in celsius_samples:
        try:
            f_temp = converter.to_fahrenheit(temp)
            k_temp = converter.to_kelvin(temp)
            print(f"{temp}°C is {f_temp:.2f}°F and {k_temp:.2f}K")
        except Exception as e:
            print(f"Error converting {temp}: {e}")
    fahrenheit_samples = [32, 212]
    print("\nFahrenheit -> Celsius:", end=" ")
    for temp_f in fahrenheit_samples:
        try:
            c_temp = converter.to_celsius(temp_f, is_kelvin=False)
            k_temp_kelvin_input = (temp_f - 32) * 5/9 + 273.15                                                                    
            print(f"{temp_f}°F is {c_temp:.2f}°C")
        except Exception as e:
            print(f"Error converting {temp_f}: {e}")
    test_inputs = ["0", "1.5"]
    print("\nString/Float Input Test:", end=" ")
    for inp in test_inputs:
        try:
            val = converter.to_celsius(inp)
            print(f"{inp} -> {val:.2f}")
        except Exception as e:
            print(f"Error with input '{inp}': {e}")
    print("\nInvalid Input Handling:", end=" ")
    try:
        converter.to_fahrenheit("not a number")
    except TypeError:
        print("Correctly caught non-numeric input for Fahrenheit conversion.")
    try:
        converter.to_celsius(10, is_kelvin=False)                                                                                   
        print(f"Valid calculation result: {converter.to_celsius(212)}")
    except Exception as e:
        print(f"Unexpected error in valid flow: {e}")