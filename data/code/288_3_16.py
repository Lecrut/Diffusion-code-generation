def celsius_to_reaumur(celsius):
    return celsius * 4 / 5

if __name__ == '__main__':
    sample_values = [0, 100, -40, 25, -20, 20]
    for value in sample_values:
        print(f"{value}°C is {celsius_to_reaumur(value)}°Re")