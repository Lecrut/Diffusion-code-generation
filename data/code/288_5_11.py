class TemperatureConverter:
    def kelvin_to_celsius(self, temp_k):
        return temp_k - 273.15

if __name__ == '__main__':
    converter = TemperatureConverter()
    temp_diff = converter.kelvin_to_celsius(300) - converter.kelvin_to_celsius(298)
    print(temp_diff)