def calculate_temperature_range(temperatures):
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    try:
        minimum = min(temperatures)
        maximum = max(temperatures)
        return maximum - minimum
    except TypeError:
        raise ValueError("All elements in the temperature list must be numbers")

if __name__ == '__main__':
    data1 = [10, 5, 20, 3]
    try:
        result1 = calculate_temperature_range(data1)
        print(result1)
    except ValueError as e:
        print(e)

    data2 = [-5, 100, 0, -10]
    try:
        result2 = calculate_temperature_range(data2)
        print(result2)
    except ValueError as e:
        print(e)