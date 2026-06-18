class CustomValueError(Exception):
    """Custom exception raised when a value is invalid."""
    pass

class CustomConversionError(CustomValueError):
    """Custom exception raised during conversion operations."""
    def __init__(self, message: str, original_value=None):
        self.original_value = original_value
        super().__init__(message)

def safe_convert(value: any, target_type: type) -> any:
    """
    Safely convert a value to the specified target type.

    Args:
        value (any): The input value to be converted.
        target_type (type): The type to which the value should be converted.

    Returns:
        any: The converted value if successful.

    Raises:
        CustomConversionError: If conversion fails or target is unsupported.
    """
    try:
        return value.__class__(value) if hasattr(value, '__new__') else type(target_type)(value)
    except (ValueError, TypeError):
        raise CustomConversionError(f"Failed to convert '{value}' to {target_type}", original_value=value)

def process_data(data_list: list) -> dict:
    """
    Process a list of values and return structured data.

    Args:
        data_list (list): List of raw inputs.

    Returns:
        dict: A dictionary containing processed results.

    Raises:
        CustomConversionError: If any item in the list cannot be converted safely.
    """
    result = {
        "input_count": len(data_list),
        "converted_items": [],
        "errors": []
    }

    for idx, item in enumerate(data_list):
        try:
            # Attempt to convert each item to an integer as a demonstration of custom handling
            converted_item = safe_convert(item, int)
            result["converted_items"].append(converted_item)
        except CustomConversionError as e:
            error_record = {
                "index": idx,
                "original_value": str(e.original_value),
                "error_message": str(e)
            }
            result["errors"].append(error_record)

    return result

if __name__ == '__main__':
    # Hard-coded sample values that do not require external input or files
    sample_data = [
        10,      # Valid int
        "25",     # String convertible to int
        None,     # Invalid for direct conversion in this context
        3.7,      # Float (will fail strict int conversion)
        True      # Boolean (valid but may behave differently based on implementation details)
    ]

    try:
        processed_result = process_data(sample_data)
        
        print("Conversion Process Completed Successfully")
        print(f"Input Count: {processed_result['input_count']}")
        if processed_result["converted_items"]:
            print(f"Converted Items: {processed_result['converted_items']}")
        else:
            print("No items were successfully converted.")

    except CustomConversionError as e:
        # This block catches errors during the processing of sample data
        error_details = [f"Index {i}: {e.original_value} -> {str(e)}" for i, item in enumerate(sample_data) if isinstance(item, (int, float)) or str(type(getattr(e, 'original_value', None))) != '<type \'NoneType\'>']
        # Re-logic error details to match the actual sample data structure for clarity
        print(f"Error Encountered: {e}")