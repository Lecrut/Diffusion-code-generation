class TemperatureConverter:
    def to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9/5) + 32
    def to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")
        return (fahrenheit - 32) * 5/9
if __name__ == '__main__':
    converter = TemperatureConverter()
    c_to_f_result = converter.to_fahrenheit(0)
    print(f"{c_to_f_result}")
    c_to_k_result = converter.to_kelvin(-40)
    print(c_to_k_result)
    f_to_c_result = converter.to_celsius(212)
    print(f"{f_to_c_result}")