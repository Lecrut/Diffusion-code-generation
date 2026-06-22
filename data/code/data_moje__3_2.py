def convert_temperatures(temperatures):
    return {location: (celsius * 9 / 5) + 32 for location, celsius in temperatures.items()}

if __name__ == '__main__':
    sample_data = {'New York': 15, 'London': 10, 'Tokyo': 25}
    print(convert_temperatures(sample_data))