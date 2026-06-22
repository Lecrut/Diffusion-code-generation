def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_less_than_100 = n < 100
    return {
        'positive': is_positive,
        'even': is_even,
        'less_than_100': is_less_than_100
    }

def process_inputs(values):
    results = []
    for val in values:
        try:
            n = int(val)
            results.append(check_number(n))
        except (ValueError, TypeError):
            results.append({'positive': False, 'even': False, 'less_than_100': False})
    return results

if __name__ == '__main__':
    sample_values = [50, -10, 105, 'abc', 200]
    output = process_inputs(sample_values)
    print(output)