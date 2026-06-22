def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    total = sum(temperatures)
    count = len(temperatures)
    return total / count

if __name__ == '__main__':
    sample_temperatures = [20.5, 22.3, 19.8, 21.0, 23.4, 18.9, 20.1]
    average = calculate_average_temperature(sample_temperatures)
    print(average)