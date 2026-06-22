def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

if __name__ == '__main__':
    sample_temps = [32, 212, 0, -40]
    min_temp_c = fahrenheit_to_celsius(min(sample_temps))
    print(f"Minimum temperature in Celsius: {min_temp_c:.2f}")