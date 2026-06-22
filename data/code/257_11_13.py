def temperature_difference(temperatures):
    if not temperatures:
        return None
    try:
        return max(temperatures) - min(temperatures)
    except TypeError:
        return "Invalid input: All elements must be numbers"

if __name__ == '__main__':
    sample_temps = [23, 17, 29, 25, 18]
    print(temperature_difference(sample_temps))