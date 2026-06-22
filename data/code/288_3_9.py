class TemperatureConverter:
    REAUMUR_PER_CELSIUS = 4 / 5

    @staticmethod
    def celsius_to_reaumur(celsius):
        return celsius * TemperatureConverter.REAUMUR_PER_CELSIUS

if __name__ == '__main__':
    sample_celsius = 0
    print(TemperatureConverter.celsius_to_reaumur(sample_celsius))
    
    sample_celsius = 100
    print(TemperatureConverter.celsius_to_reaumur(sample_celsius))
    
    sample_celsius = -40
    print(TemperatureConverter.celsius_to_reaumur(sample_celsius))