def calculate_average_temperature(readings):
    if not readings:
        return 0.0
    return sum(readings) / len(readings)

if __name__ == '__main__':
    samples = [20.5, 21.0, 22.5, 20.0, 21.5]
    result = calculate_average_temperature(samples)
    print(result)