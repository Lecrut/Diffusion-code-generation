def temperature_difference(temperatures):
    if not temperatures:
        return 0
    try:
        return max(temperatures) - min(temperatures)
    except TypeError:
        return "Invalid input: All elements must be numbers"

if __name__ == '__main__':
    sample_temps = [32, 45, 19, 67, 28]
    print(temperature_difference(sample_temps))