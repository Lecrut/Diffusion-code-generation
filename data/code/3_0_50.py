class TemperatureCalculator:
    MIN_TEMPERATURE = -100.0
    MAX_TEMPERATURE = 150.0

    @staticmethod
    def validate_temperatures(temperatures):
        if not temperatures:
            raise ValueError("The list of temperatures cannot be empty.")
        for temp in temperatures:
            if not (TemperatureCalculator.MIN_TEMPERATURE <= temp <= TemperatureCalculator.MAX_TEMPERATURE):
                raise ValueError(f"Temperature {temp} is out of valid range.")

    @staticmethod
    def calculate_average_temperature(temperatures):
        TemperatureCalculator.validate_temperatures(temperatures)
        return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [26.5, 27.1, 25.8, 26.9, 27.0]
    average_temperature = TemperatureCalculator.calculate_average_temperature(sample_temperatures)
    print(average_temperature)