def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [72.5, 75.0, 70.5, 68.0, 73.5]
    average = calculate_average_temperature(sample_temperatures)
    print(average)