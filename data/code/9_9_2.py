class ConversionError(Exception):
    pass
class InvalidSourceDataError(ConversionError):
    pass
class DataTypeError(ConversionError):
    pass
def convert_data(source_data):
    if not isinstance(source_data, list):
        raise InvalidSourceDataError("Source data must be a list.")
    results = []
    for item in source_data:
        if not isinstance(item, (int, float)):
            raise DataTypeError(f"Item {item} is not a valid number.")
        try:
            converted_value = float(item)
            results.append(converted_value)
        except ValueError:
            raise DataTypeError(f"Could not convert item '{item}' to float.")
    return results
if __name__ == '__main__':
    sample_input_valid = [10, 25.5, 30]
    sample_input_invalid_type = [10, "twenty", 30]
    sample_input_empty = []
    sample_input_mixed = [10, 25, "error", 30.5]
    try:
        result1 = convert_data(sample_input_valid)
        print(f"Valid conversion result: {result1}")
    except ConversionError as e:
        print(f"Error during valid conversion attempt: {e}")
    try:
        convert_data(sample_input_invalid_type)
    except DataTypeError as e:
        print(f"Caught expected DataTypeError for invalid types: {e}")
    except ConversionError as e:
        print(f"Caught unexpected ConversionError: {e}")
    try:
        result3 = convert_data(sample_input_empty)
        print(f"Empty list result: {result3}")
    except ConversionError as e:
        print(f"Error during empty list conversion attempt: {e}")
    try:
        convert_data(sample_input_mixed)
    except DataTypeError as e:
        print(f"Caught expected DataTypeError for mixed data: {e}")
    except ConversionError as e:
        print(f"Caught unexpected ConversionError: {e}")