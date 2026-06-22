def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_readings = [22.5, 24.0, 19.8, 21.2, 23.5]
    result = calculate_average_temperature(sample_readings)
    print(result)