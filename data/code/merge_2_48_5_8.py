import sys
def advanced_divide(numerator: float | int = None, denominator: float | int = None) -> dict[str, any]:
    if numerator is None and not isinstance(denominator, (int, float)):
        raise TypeError("Numerator must be a number.")
    result_value = 0.0
    error_message = ""
    try:
        num_val = int(numerator) if isinstance(numerator, int) else float(numerator)
        den_val = int(denominator) if isinstance(denominator, int) else float(denominator)
        if den_val == 0.0:
            error_message = "Division by zero."
        else:
            result_value = num_val / den_val
    except ZeroDivisionError as e:
        error_message = str(e)
    return {
        'input_numerator': numerator,
        'input_denominator': denominator,
        'result_type': type(result_value).__name__,
        'result_value': result_value if not error_message else None,
        'error': error_message if error_message else "None"
    }
if __name__ == '__main__':
    output = advanced_divide(100.5, 2)
    print("=== Division Report ===")
    print(f"Numerator: {output['input_numerator']} (Type: {type(output['input_numerator']).__name__})")
    print(f"Denominator: {output['input_denominator']} (Type: {type(output['input_denominator']).__name__})")
    if output['error']:
        print(f"Error: {output['error']}")
    else:
        print(f"Result Value: {output['result_value']} ({output['result_type']})")