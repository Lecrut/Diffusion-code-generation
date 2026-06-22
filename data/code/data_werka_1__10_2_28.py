def calculate_temperature_difference(t_actual, t_expected):
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    t_actual = 25.0
    t_expected = 30.0
    difference = calculate_temperature_difference(t_actual, t_expected)
    print(difference)