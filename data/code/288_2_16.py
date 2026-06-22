def validate_temperatures(temperatures):
    if not all(isinstance(temp, (int, float)) for temp in temperatures):
        raise ValueError("All temperatures must be numbers.")

def calculate_average_celsius(temperatures):
    validate_temperatures(temperatures)
    return sum(temperatures) / len(temperatures)

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [10, 20, 30, 40]
    average_celsius = calculate_average_celsius(sample_temps)
    average_fahrenheit = celsius_to_fahrenheit(average_celsius)
    print(f"Average temperature in Fahrenheit: {average_fahrenheit:.2f}")