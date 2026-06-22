def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    temps = [20.5, 21.0, 19.5, 22.0, 20.0]
    result = calculate_average_temperature(temps)
    print(result)