def convert_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    sample_temps_f = [32, 212, 0, -40]
    min_temp_c = convert_to_celsius(min(sample_temps_f))
    print(f"Minimum temperature in Celsius: {min_temp_c:.2f}")