import sys
def advanced_divide(dividend: int | float, divisor: int | float) -> dict[str, any]:
    result = {
        "dividend_type": type(dividend).__name__,
        "divisor_type": type(divisor).__name__,
        "result_value": dividend / divisor if divisor != 0 else None,
        "is_valid_operation": True,
        "error_message": None,
    }
    if divisor == 0:
        result["is_valid_operation"] = False
        result["error_message"] = "Division by zero is undefined."
        return result
    try:
        precision_result = round(dividend / divisor, 12)
        result["result_value"] = float(precision_result) if isinstance(result["result_value"], int) else result["result_value"]
    except Exception as e:
        result["is_valid_operation"] = False
        result["error_message"] = f"An error occurred during calculation: {str(e)}"
    return result
if __name__ == '__main__':
    sample_dividend = 10.5
    sample_divisor = 3
    output_data = advanced_divide(sample_dividend, sample_divisor)
    print(f"Dividend Type: {output_data['dividend_type']}")
    print(f"Divisor Type: {output_data['divisor_type']}")
    if output_data["is_valid_operation"]:
        print(f"Result Value: {output_data['result_value']}")
    else:
        print(f"Error Message: {output_data['error_message']}")