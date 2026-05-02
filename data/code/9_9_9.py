class ConversionError(Exception):
    pass
class DataValidationError(ConversionError):
    pass
class FileReadError(ConversionError):
    pass
def convert_data(input_data, conversion_factor):
    if not isinstance(input_data, list):
        raise DataValidationError("Input data must be a list.")
    if not isinstance(conversion_factor, (int, float)):
        raise DataValidationError("Conversion factor must be a number.")
    result = []
    for item in input_data:
        if not isinstance(item, (int, float)):
            raise DataValidationError(f"Item {item} is not a number.")
        try:
            converted_value = item * conversion_factor
            result.append(converted_value)
        except TypeError:
            raise DataValidationError(f"Error during multiplication for item: {item}")
    return result
if __name__ == '__main__':
    sample_input = [10, 25, 50, "error", 100]
    sample_factor = 2.5
    try:
        converted = convert_data(sample_input, sample_factor)
        print(converted)
    except DataValidationError as e:
        print(f"Data Validation Error: {e}")
    except FileReadError as e:
        print(f"File Read Error: {e}")
    except ConversionError as e:
        print(f"General Conversion Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")