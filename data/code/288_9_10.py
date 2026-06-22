def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    sample_temps_f = [32.0, 212.0, 68.0]
    min_temp_c = fahrenheit_to_celsius(min(sample_temps_f))
    print(f"Minimum temperature in Celsius: {min_temp_c:.2f}")