def analyze_integers(a, b, c):
    analyzed_values = []
    for current_number in [a, b, c]:
        if not isinstance(current_number, int):
            raise ValueError("All inputs must be integers")
        value_status = {
            'number': current_number,
            'is_positive': current_number > 0,
            'is_even': current_number % 2 == 0,
            'is_below_100': current_number < 100
        }
        analyzed_values.append(value_status)
    return analyzed_values

if __name__ == '__main__':
    input_a = 7
    input_b = -20
    input_c = 99
    result_data = analyze_integers(input_a, input_b, input_c)
    print(result_data)