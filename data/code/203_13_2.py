import sys
def compare_quantities(q1_str, q2_str):
    try:
        q1 = float(q1_str)
        q2 = float(q2_str)
    except ValueError:
        return "Error: Invalid input. Both quantities must be valid numbers."
    if q1 > q2:
        result = f"{q1} is greater than {q2}"
    elif q1 < q2:
        result = f"{q1} is less than {q2}"
    else:
        result = f"{q1} is equal to {q2}"
    return result
if __name__ == '__main__':
    sample_q1 = "45.7"
    sample_q2 = "120.3"
    comparison_result = compare_quantities(sample_q1, sample_q2)
    print(f"Quantity 1: {sample_q1}")
    print(f"Quantity 2: {sample_q2}")
    print("-" * 30)
    print(comparison_result)