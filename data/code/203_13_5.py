import sys
def compare_quantities(a, b):
    results = {}
    try:
        if a > b:
            results['a_is_greater'] = True
            results['difference'] = a - b
        elif a < b:
            results['b_is_greater'] = True
            results['difference'] = b - a
        else:
            results['are_equal'] = True
            results['difference'] = 0
    except TypeError:
        results['error'] = "Type mismatch during comparison"
    return results
if __name__ == '__main__':
    input_data = [15, 22]
    if len(input_data) < 2:
        print("Error: Insufficient input provided.")
    else:
        try:
            val1 = float(input_data[0])
            val2 = float(input_data[1])
            comparison_results = compare_quantities(val1, val2)
            print("--- Quantity Comparison ---")
            if 'error' in comparison_results:
                print(f"Error: {comparison_results['error']}")
            else:
                if 'are_equal' in comparison_results:
                    print(f"Quantity 1: {val1}")
                    print(f"Quantity 2: {val2}")
                    print("Result: The quantities are equal.")
                elif 'a_is_greater' in comparison_results:
                    diff = comparison_results['difference']
                    print(f"Quantity 1: {val1}")
                    print(f"Quantity 2: {val2}")
                    print(f"Result: Quantity 1 is greater than Quantity 2 by {diff}.")
                elif 'b_is_greater' in comparison_results:
                    diff = comparison_results['difference']
                    print(f"Quantity 1: {val1}")
                    print(f"Quantity 2: {val2}")
                    print(f"Result: Quantity 2 is greater than Quantity 1 by {diff}.")
                else:
                    print("Comparison failed due to an unexpected state.")
        except ValueError:
            print("Error: Invalid input. Please ensure inputs are valid numeric values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")