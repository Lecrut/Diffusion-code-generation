def calculate_temperature_difference(actual, expected):
    return abs(actual - expected)

if __name__ == '__main__':
    t_actual = 25.3
    t_expected = 20.7
    difference = calculate_temperature_difference(t_actual, t_expected)
    print(difference)