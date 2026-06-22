def calculate_temperature_difference(t_actual, t_expected):
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    actual_temp = 30.0
    expected_temp = 28.5
    temp_difference = calculate_temperature_difference(actual_temp, expected_temp)
    print(temp_difference)