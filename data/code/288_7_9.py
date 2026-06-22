def max_temp_celsius_to_fahrenheit(temps):
    max_c = max(temps)
    return (max_c * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [20, 25, 18, 30, 22]
    print(max_temp_celsius_to_fahrenheit(sample_temps))