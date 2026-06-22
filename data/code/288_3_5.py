class TemperatureConverter:
    def celsius_to_reaumur(self, celsius):
        return celsius * 4 / 5

if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.celsius_to_reaumur(0))
    print(converter.celsius_to_reaumur(100))
    print(converter.celsius_to_reaumur(-40))