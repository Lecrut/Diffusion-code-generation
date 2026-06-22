def calculate_temperature_range(temperatures):
    if not temperatures:
        return 0
    minimum = min(temperatures)
    maximum = max(temperatures)
    return maximum - minimum

if __name__ == '__main__':
    data1 = [10, 5, 20, 3]
    result1 = calculate_temperature_range(data1)
    print(result1)
    data2 = [-5, 100, 0, -10]
    result2 = calculate_temperature_range(data2)
    print(result2)