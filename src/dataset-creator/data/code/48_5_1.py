import sys
def divide_numbers(a: float | int = 0, b: float | int = 1) -> dict[str, any]:
    result_value = a / b
    if isinstance(result_value, (int, float)):
        is_integer_result = result_value == int(result_value)
        output_data: dict[str, any] = {
            "input_a": a,
            "type_a": type(a).__name__,
            "input_b": b,
            "type_b": type(b).__name__,
            "result": result_value if not is_integer_result else int(result_value),
            "is_exact_integer": is_integer_result,
            "operation_type": "division"
        }
    else:
        output_data = {
            "input_a": a,
            "type_a": type(a).__name__,
            "input_b": b,
            "type_b": type(b).__name__,
            "result": result_value,
            "is_exact_integer": False,
            "operation_type": "division"
        }
    return output_data
if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 2
    report = divide_numbers(sample_a, sample_b)
    print(f"Input A: {report['input_a']} ({report['type_a']})")
    print(f"Input B: {report['input_b']} ({report['type_b']})")
    print(f"Result: {report['result']} (Exact Integer: {report['is_exact_integer']})")