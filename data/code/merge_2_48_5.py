import sys
def divide_advanced(a: float | int, b: float | int) -> dict[str, any]:
    result = {
        "input_a": a,
        "type_a": type(a).__name__,
        "input_b": b,
        "type_b": type(b).__name__,
        "operation": f"{a} / {b}",
        "result_raw": None,
        "error": None,
    }
    if isinstance(b, (int, float)) and b == 0:
        result["error"] = "Division by zero is undefined."
        return result
    try:
        raw_result = a / b
        if type(a).__name__ in ("float",) or type(b).__name__ in ("float",):
            decimal_places = 6
            formatted_result = f"{raw_result:.{decimal_places}f}"
        else:
            integer_part, remainder = divmod(int(raw_result), int(abs(raw_result))) if raw_result != 0 else (int(a // b), a % b)
            formatted_result = str(round(raw_result, decimal_places))
        result["result_raw"] = round(raw_result, decimal_places)
        result["formatted_output"] = formatted_result
    except Exception as e:
        result["error"] = f"Calculation failed: {str(e)}"
    return result
if __name__ == '__main__':
    sample_a = 17.5
    sample_b = 4
    output_data = divide_advanced(sample_a, sample_b)
    print("=" * 60)
    print("DIVISION REPORT")
    print("-" * 60)
    print(f"Input A: {output_data['input_a']} ({output_data['type_a']})")
    print(f"Input B: {output_data['input_b']} ({output_data['type_b']})")
    print(f"Operation: {output_data['operation']}")
    if output_data["error"]:
        print("-" * 60)
        print("ERROR:", output_data["error"])
    else:
        print("-" * 60)
        print(f"Result (Raw): {output_data['result_raw']}")
        print(f"Formatted Output: {output_data.get('formatted_output', 'N/A')}")
    print("=" * 60)