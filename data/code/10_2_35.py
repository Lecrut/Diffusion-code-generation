def calculate_temperature_difference(actual, expected):
    return abs(actual - expected)

if __name__ == '__main__':
    t_actual = 25.0
    t_expected = 23.5
    difference = calculate_temperature_difference(t_actual, t_expected)
    print(difference)