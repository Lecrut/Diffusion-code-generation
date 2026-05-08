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
        results = process_numbers(a, b, c)
        print(f"Results for inputs ({a}, {b}, {c}):")
        print(f"A checks: {results.get('a_positive')}, {results.get('a_even')}, {results.get('a_less_than_100')}")
        print(f"B checks: {results.get('b_positive')}, {results.get('b_even')}, {results.get('b_less_than_100')}")
        print(f"C checks: {results.get('c_positive')}, {results.get('c_even')}, {results.get('c_less_than_100')}")
    except Exception as e:
        print(f"An error occurred during processing: {e}")