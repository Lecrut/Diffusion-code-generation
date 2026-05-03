class ConversionError(Exception):
    pass
class DataValidationError(ConversionError):
    pass
class FileReadError(ConversionError):
    pass
def convert_data(input_data):
    if not isinstance(input_data, list):
        raise DataValidationError("Input must be a list.")
    results = []
    for item in input_data:
        if not isinstance(item, dict):
            raise DataValidationError(f"Item {item} is not a dictionary.")
        try:
            key = item['key']
            value = item['value']
            if not isinstance(key, str) or not isinstance(value, (int, float)):
                raise DataValidationError(f"Key must be a string and value must be numeric in item: {item}")
            converted_value = float(value)
            results.append({"key": key, "converted": converted_value})
        except KeyError as e:
            raise DataValidationError(f"Missing required key in item: {item}. Missing key: {e}") from e
        except ValueError as e:
            raise DataValidationError(f"Value could not be converted to float in item: {item}. Error: {e}") from e
    return results
if __name__ == '__main__':
    sample_input = [
        {"key": "A", "value": "10.5"},
        {"key": "B", "value": "20"},
        {"key": "C", "value": "invalid"}
    ]
    try:
        converted = convert_data(sample_input)
        print(converted)
    except ConversionError as e:
        print(f"Conversion failed with a specific error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")