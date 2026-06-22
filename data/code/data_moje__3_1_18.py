def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_readings = [20.5, 21.0, 19.8, 22.3, 20.1]
    result = calculate_average_temperature(sample_readings)
    print(result)