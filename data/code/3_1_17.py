def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temps = [20.5, 21.3, 19.8, 22.1, 20.0]
    average = calculate_average_temperature(sample_temps)
    print(average)