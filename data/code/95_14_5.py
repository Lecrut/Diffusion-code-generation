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
    input_a = 10
    input_b = 50
    input_c = 150
    try:
        numbers = [input_a, input_b, input_c]
        if len(numbers) != 3:
            raise ValueError("Incorrect number of inputs provided.")
        results = process_numbers(input_a, input_b, input_c)
        print(results)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Inputs must be integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")