def temperature_difference(temperatures):
    if not temperatures:
        return None
    try:
        min_temp = min(temperatures)
        max_temp = max(temperatures)
        return max_temp - min_temp
    except TypeError:
        return None

if __name__ == '__main__':
    sample_temps = [23, 17, 29, 15, 30]
    print(temperature_difference(sample_temps))