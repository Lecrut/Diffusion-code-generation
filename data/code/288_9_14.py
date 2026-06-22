def min_temp_fahrenheit_to_celsius(temps):
    return min(temp - 32 * 5 / 9 for temp in temps)

if __name__ == '__main__':
    sample_temps = [32, 0, -40, 100]
    print(min_temp_fahrenheit_to_celsius(sample_temps))