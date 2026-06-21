def calculate_average_temperature(temperatures):
    def validate_temperatures(temp_list):
        if not temp_list:
            raise ValueError("The list of temperatures cannot be empty.")
        if not all(isinstance(t, (int, float)) for t in temp_list):
            raise ValueError("All elements in the temperature list must be numbers.")

    validate_temperatures(temperatures)
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [24.5, 26.0, 23.8, 22.9, 25.1]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)