def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_readings = [20.5, 22.1, 19.8, 23.4, 21.0]
    result = calculate_average_temperature(sample_readings)
    print(result)