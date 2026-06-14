import sys
def compare_quantities(q1_str, q2_str):
    try:
        q1 = float(q1_str)
        q2 = float(q2_str)
    except ValueError:
        return None, "Error: Invalid input. Both values must be numeric."
    if q1 > q2:
        result = f"{q1} is greater than {q2}"
    elif q1 < q2:
        result = f"{q1} is less than {q2}"
    else:
        result = f"{q1} is equal to {q2}"
    return result, None
if __name__ == '__main__':
    sample_input_1 = "45.7"
    sample_input_2 = "12.3"
    result, error = compare_quantities(sample_input_1, sample_input_2)
    if error:
        print(error)
    else:
        print("--- Quantity Comparison ---")
        print(f"Quantity 1: {sample_input_1}")
        print(f"Quantity 2: {sample_input_2}")
        print("-" * 30)
        print(result)