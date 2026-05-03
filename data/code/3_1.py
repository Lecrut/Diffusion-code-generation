def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)
if __name__ == '__main__':
    sample_temps = [22.5, 23.1, 21.9, 24.0, 22.8]
    average = calculate_average_temperature(sample_temps)
    print(average)