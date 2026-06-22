class TemperatureCalculator:
    KELVIN_TO_CELSIUS_OFFSET = 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - TemperatureCalculator.KELVIN_TO_CELSIUS_OFFSET

    @staticmethod
    def average_temperature(temp1, temp2, temp3):
        celsius_temp1 = TemperatureCalculator.fahrenheit_to_celsius(temp1) if temp1 > 0 else temp1
        celsius_temp2 = TemperatureCalculator.fahrenheit_to_celsius(temp2) if temp2 > 0 else temp2
        celsius_temp3 = TemperatureCalculator.kelvin_to_celsius(temp3) if temp3 >= 0 else temp3
        
        return (celsius_temp1 + celsius_temp2 + celsius_temp3) / 3

if __name__ == '__main__':
    converter = TemperatureCalculator()
    avg_temp = converter.average_temperature(77, -40, 300)
    print(f"Average temperature: {avg_temp}°C")