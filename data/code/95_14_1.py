def process_numbers(a, b, c):
    results = {}
    if a > 0:
        results['a_positive'] = True
    else:
        results['a_positive'] = False
    if a % 2 == 0:
        results['a_even'] = True
    else:
        results['a_even'] = False
    if a < 100:
        results['a_less_than_100'] = True
    else:
        results['a_less_than_100'] = False
    if b > 0:
        results['b_positive'] = True
    else:
        results['b_positive'] = False
    if b % 2 == 0:
        results['b_even'] = True
    else:
        results['b_even'] = False
    if b < 100:
        results['b_less_than_100'] = True
    else:
        results['b_less_than_100'] = False
    if c > 0:
        results['c_positive'] = True
    else:
        results['c_positive'] = False
    if c % 2 == 0:
        results['c_even'] = True
    else:
        results['c_even'] = False
    if c < 100:
        results['c_less_than_100'] = True
    else:
        results['c_less_than_100'] = False
    return results
if __name__ == '__main__':
    input_values = (10, 25, 99)
    a, b, c = input_values
    try:
        processed_data = process_numbers(a, b, c)
        print(processed_data)
    except Exception as e:
        print(f"An error occurred during processing: {e}")