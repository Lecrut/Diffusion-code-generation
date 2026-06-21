def calculate_temperature_difference(t_actual, t_expected):
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    sample_values = [
        (23.5, 25.0),
        (25.5, 23.0),
        (25.3, 27.8),
        (25.3, 20.8)
    ]
    
    for t_actual, t_expected in sample_values:
        difference = calculate_temperature_difference(t_actual, t_expected)
        print(f"Difference between {t_actual} and {t_expected}: {difference}")