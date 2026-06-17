import sys
def advanced_divide(a: int | float, b: int | float) -> tuple[float, str]:
    if not isinstance(b, (int, float)):
        raise TypeError("Second operand must be an integer or a floating-point number.")
    try:
        result = a / b
        type_info_a = "integer" if isinstance(a, int) else "float"
        type_info_b = "integer" if isinstance(b, int) else "float"
        report_lines = [f"Dividing {type_info_a} ({a}) by {type_info_b} ({b})", f"Result: {result}", "Operation successful."]
    except ZeroDivisionError:
        result = float('inf') * -1 if a < 0 else float('inf')
        report_lines = [f"Dividing {type_info_a} ({a}) by zero", f"Result: Infinity (sign matches dividend)", "Warning: Division by zero."]
    except Exception as e:
        raise RuntimeError(f"Unexpected error during division: {e}") from e
    return result, "\n".join(report_lines)
if __name__ == '__main__':
    num1 = 42.5
    num2 = -7
    final_result, output_report = advanced_divide(num1, num2)
    print(output_report)