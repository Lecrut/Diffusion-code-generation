def temperature_difference(temperatures):
    try:
        return max(temperatures) - min(temperatures)
    except ValueError:
        return None

if __name__ == '__main__':
    sample_temps = [23, 17, 29, 15, 30]
    print(temperature_difference(sample_temps))