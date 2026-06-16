def convert_temperature(temp_celsius, to_fahrenheit=None, to_kelvin=None):
    if to_fahrenheit is not None:
        return (temp_celsius * 9/5) + 32
    elif to_kelvin is not None:
        return temp_celsius + 273.15
    else:
        return temp_celsius
if __name__ == '__main__':
    sample_celsius = 25.0
    fahrenheit = convert_temperature(sample_celsius, to_fahrenheit=True)
    kelvin = convert_temperature(sample_celsius, to_kelvin=True)
    celsius_only = convert_temperature(sample_celsius)
    print(f"25.0 C is {fahrenheit:.2f} F")
    print(f"25.0 C is {kelvin:.2f} K")
    print(f"25.0 C (original) is {celsius_only:.2f}")