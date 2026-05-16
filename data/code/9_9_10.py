class ConversionError(Exception):
    pass
class InvalidSourceError(ConversionError):
    pass
class InvalidTargetError(ConversionError):
    pass
def convert_data(source_data, target_type):
    if not isinstance(source_data, (list, tuple)):
        raise InvalidSourceError("Source data must be a list or tuple.")
    if not isinstance(target_type, type):
        raise InvalidTargetError("Target type must be a Python type.")
    if not source_data:
        raise ConversionError("Source data cannot be empty.")
    result = []
    for item in source_data:
        try:
            if target_type is int:
                converted_item = int(item)
            elif target_type is float:
                converted_item = float(item)
            elif target_type is str:
                converted_item = str(item)
            else:
                raise InvalidTargetError(f"Unsupported target type: {target_type}")
            result.append(converted_item)
        except ValueError as e:
            raise ConversionError(f"Failed to convert item '{item}' to {target_type.__name__}: {e}")
        except Exception as e:
            raise ConversionError(f"An unexpected error occurred during conversion of '{item}': {e}")
    return result
if __name__ == '__main__':
    sample_source = [10, "25.5", "30", "invalid_num"]
    sample_target_int = int
    sample_target_float = float
    sample_target_str = str
    print("--- Converting to Integer ---")
    try:
        result_int = convert_data(sample_source, sample_target_int)
        print(f"Result (int): {result_int}")
    except ConversionError as e:
        print(f"Error during integer conversion: {e}")
    print("\n--- Converting to Float ---")
    try:
        result_float = convert_data(sample_source, sample_target_float)
        print(f"Result (float): {result_float}")
    except ConversionError as e:
        print(f"Error during float conversion: {e}")
    print("\n--- Converting to String ---")
    try:
        result_str = convert_data(sample_source, sample_target_str)
        print(f"Result (str): {result_str}")
    except ConversionError as e:
        print(f"Error during string conversion: {e}")
    print("\n--- Testing Invalid Source ---")
    try:
        convert_data("not a list", int)
    except InvalidSourceError as e:
        print(f"Caught expected error: {e}")
    except ConversionError as e:
        print(f"Caught unexpected error type: {e}")
    print("\n--- Testing Empty Source ---")
    try:
        convert_data([], int)
    except ConversionError as e:
        print(f"Caught expected error: {e}")