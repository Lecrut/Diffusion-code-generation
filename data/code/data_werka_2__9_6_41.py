class ConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidInputTypeError(ConversionError):
    def __init__(self, value_type):
        super().__init__(f'Invalid input type: {value_type}')

class ConversionFailedException(ConversionError):
    def __init__(self, value):
        super().__init__(f'Conversion failed for value: {value}')

def convert_to_int(value):
    if not isinstance(value, str):
        raise InvalidInputTypeError(type(value).__name__)
    
    try:
        return int(value)
    except ValueError as e:
        raise ConversionFailedException(value) from e

def safe_conversion(values):
    results = []
    for value in values:
        try:
            converted_value = convert_to_int(value)
            results.append(converted_value)
        except InvalidInputTypeError as iite:
            print(f"Error: {iite}")
        except ConversionFailedException as cfe:
            print(f"Error: {cfe}")
    return results

if __name__ == '__main__':
    sample_values = ['123', 'abc', '456.78', '-90']
    conversion_results = safe_conversion(sample_values)
    for result in conversion_results:
        print(result)