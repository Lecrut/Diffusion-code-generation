def celsius_to_fahrenheit(celsius_list):
    def convert_single(temp):
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature must be an integer or float.")
        return temp * 9/5 + 32

    return [convert_single(c) for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 100, 37]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)