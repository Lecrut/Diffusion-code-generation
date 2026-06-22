def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_less_than_100 = n < 100
    return {
        'value': n,
        'is_positive': is_positive,
        'is_even': is_even,
        'is_less_than_100': is_less_than_100
    }

def process_inputs(values):
    results = []
    for val in values:
        try:
            num = int(val)
            results.append(check_number(num))
        except (ValueError, TypeError):
            results.append({
                'value': val,
                'is_positive': False,
                'is_even': False,
                'is_less_than_100': False,
                'error': 'Invalid input'
            })
    return results

if __name__ == '__main__':
    sample_values = [50, -10, 105]
    processed = process_inputs(sample_values)
    for item in processed:
        print(item)