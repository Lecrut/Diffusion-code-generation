import sys
def divide_advanced(a: float | int = 0, b: float | int = 1) -> dict[str, any]:
    result_value = a / b
    if isinstance(result_value, (int, float)):
        is_integer_result = result_value == int(result_value)
        output_report = {
            "input_a": a,
            "type_a": type(a).__name__,
            "input_b": b,
            "type_b": type(b).__name__,
            "result": float(result_value),
            "is_exact_integer": is_integer_result,
            "integer_representation": int(result_value) if is_integer_result else None,
            "operation_status": "success"
        }
    else:
        output_report = {
            "input_a": a,
            "type_a": type(a).__name__,
            "input_b": b,
            "result": result_value,
            "is_exact_integer": False,
            "integer_representation": None,
            "operation_status": "success" if not (a % b) else "error: division by zero or non-numeric input",
            "exception_message": str(result_value) if isinstance(result_value, Exception) else ""
        }
    return output_report
if __name__ == '__main__':
    sample_data = {
        'int_div_int': divide_advanced(10, 3),
        'float_div_float': divide_advanced(4.5, 2.0),
        'mixed_types': divide_advanced(-7, -2)
    }
    for label, data in sample_data.items():
        print(f"--- {label} ---")
        print("Input A:", data['input_a'], "(Type:)", data['type_a'])
        print("Input B:", data['input_b'], "(Type:)", data['type_b'])
        print("Result:", data['result'])
        if 'integer_representation' in data and data['integer_representation'] is not None:
            print("Exact Integer Form:", data['integer_representation'])
        else:
            print("Is Exact Integer?", "Yes" if data.get('is_exact_integer') else "No")
        print("Status:", data['operation_status'])
        print()