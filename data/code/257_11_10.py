def temperature_difference(temperatures):
    if not temperatures:
        return None
    try:
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        return max_temp - min_temp
    except ValueError:
        return None

if __name__ == '__main__':
    sample_temps = [23, 17, 29, 25, 18]
    print(temperature_difference(sample_temps))