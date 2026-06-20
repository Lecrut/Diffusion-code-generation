def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [22.5, 23.1, 19.8, 25.3, 21.4]
    result = calculate_average_temperature(sample_temperatures)
    print(result)