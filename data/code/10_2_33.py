def calculate_temperature_difference(actual, expected):
    return abs(actual - expected)

if __name__ == '__main__':
    t_actual = 23.5
    t_expected = 20.0
    difference = calculate_temperature_difference(t_actual, t_expected)
    print(difference)