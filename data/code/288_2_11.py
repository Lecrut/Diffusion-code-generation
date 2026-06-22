def avg_temp_celsius_to_fahrenheit(temps):
    avg_celsius = sum(temps) / len(temps)
    return (avg_celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [10, 20, 30, 40, 50]
    print(avg_temp_celsius_to_fahrenheit(sample_temps))