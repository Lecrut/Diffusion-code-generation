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

def convert_to_float(value):
    if not isinstance(value, str):
        raise InvalidInputTypeError(type(value).__name__)
    try:
        return float(value)
    except ValueError as e:
        raise ConversionFailedException(value) from e

def safe_conversion(values):
    results = []
    for value in values:
        try:
            int_result = convert_to_int(value)
            float_result = convert_to_float(value)
            results.append((int_result, float_result))
        except InvalidInputTypeError as e:
            print(f'Error: {e}')
        except ConversionFailedException as e:
            print(f'Error: {e}')
    return results

if __name__ == '__main__':
    sample_values = ['123', '45.67', 'abc', '0']
    conversion_results = safe_conversion(sample_values)
    for result in conversion_results:
        print(result)