class TemperatureConverter:
    def __init__(self):
        self.KELVIN_OFFSET = 273.15

    def kelvin_to_celsius(self, kelvin_list):
        celsius_list = []
        for temp in kelvin_list:
            if isinstance(temp, (int, float)) and temp >= 0:
                celsius_list.append(temp - self.KELVIN_OFFSET)
            else:
                celsius_list.append(None)
        return celsius_list

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_kelvin_values = [0, 273.15, 300, 400, -100, 'abc', None]
    converted_values = converter.kelvin_to_celsius(sample_kelvin_values)
    print(converted_values)