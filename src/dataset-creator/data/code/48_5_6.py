import sys
def divide_advanced(a: float | int, b: float | int) -> dict[str, any]:
    if not isinstance(b, (int, float)) or b == 0:
        return {"error": "Division by zero or invalid numeric input", "status_code": 400}
    original_a_type = type(a).__name__
    original_b_type = type(b).__name__
    result_value = a / b
    inferred_result_type = type(result_value).__name__ if isinstance(result_value, float) else 'int'
    output_report = {
        "input": {"a": a, "b": b},
        "types": {"input_a": original_a_type, "input_b": original_b_type, "result": inferred_result_type},
        "operation": f"{original_a_type} / {original_b_type}",
        "calculation_details": {
            "numerator": a,
            "denominator": b,
            "quotient": result_value,
            "precision_used": 15 if isinstance(result_value, float) else None
        },
        "status_code": 200,
        "message": f"Division successful: {a} / {b} = {result_value}"
    }
    return output_report
if __name__ == '__main__':
    sample_input_a = 17.5
    sample_input_b = 4
    result_data = divide_advanced(sample_input_a, sample_input_b)
    print(f"Input A ({sample_input_a}) type: {type(sample_input_a).__name__}")
    print(f"Input B ({sample_input_b}) type: {type(sample_input_b).__name__}")
    print("-" * 40)
    if "error" in result_data:
        print(result_data["message"])
    else:
        calc_details = result_data["calculation_details"]
        print(f"Numerator: {calc_details['numerator']}")
        print(f"Denominator: {calc_details['denominator']}")
        print(f"Quotient ({type(calc_details['quotient']).__name__}): {calc_details['quotient']}")
    print("-" * 40)
    print(result_data["message"])