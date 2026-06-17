import math
from typing import Union
def advanced_divide(dividend: float, divisor: float) -> dict[str, any]:
    try:
        dividend_type = "int" if isinstance(dividend, int) else "float"
        if divisor == 0:
            return {
                "status": "error",
                "message": "Division by zero is undefined.",
                "dividend_input_type": dividend_type,
                "input_values": [str(dividend), str(divisor)]
            }
        quotient = dividend / divisor
        if isinstance(dividend, int) and isinstance(divisor, int):
            remainder = dividend % divisor
            if math.isclose(quotient, round(quotient)):
                return {
                    "status": "success",
                    "message": f"Division completed successfully.",
                    "dividend_input_type": dividend_type,
                    "input_values": [str(dividend), str(divisor)],
                    "result": quotient if isinstance(quotient, int) else round(quotient),
                    "remainder": remainder,
                    "exact_integer_result": True
                }
        abs_error = abs(dividend - (divisor * quotient)) / divisor
        return {
            "status": "success",
            "message": f"Division completed successfully.",
            "dividend_input_type": dividend_type,
            "input_values": [str(dividend), str(divisor)],
            "result": quotient if isinstance(quotient, int) else round(quotient, 10),
            "remainder": None,
            "percentage_error": abs_error * 100,
            "exact_integer_result": False
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"An unexpected error occurred during division.",
            "dividend_input_type": dividend_type if 'dividend' in locals() else "unknown",
            "input_values": [str(dividend), str(divisor)],
            "exception_details": {
                "type": type(e).__name__,
                "value": str(e)
            }
        }
if __name__ == '__main__':
    sample_dividend = 105.7
    sample_divisor = 23
    result_data = advanced_divide(sample_dividend, sample_divisor)
    print(f"Operation Result: {result_data['status']}")
    if 'message' in result_data and isinstance(result_data.get('exception_details'), dict):
        details = result_data.get('exception_details')
        error_type = details.get('type', 'Unknown Error')
        error_value = details.get('value', str(details))
        print(f"Error Type: {error_type}")
    else:
        message = result_data['message'] if isinstance(result_data, dict) and 'message' in result_data else "No specific status message."
        print(message)