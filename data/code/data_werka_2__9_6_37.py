class ConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidInputTypeError(ConversionError):
    def __init__(self, value):
        super().__init__(f'Invalid input type: {value}')

class ConversionFailedException(ConversionError):
    def __init__(self, value):
        super().__init__(f'Conversion failed for value: {value}')

def convert_to_int(value):
    if not isinstance(value, str):
        raise InvalidInputTypeError(f'Expected a string but got {type(value).__name__}')
    try:
        return int(value)
    except ValueError as e:
        raise ConversionFailedException(value) from e

if __name__ == '__main__':
    sample_values = ['123', 'abc', '456.78', '-90']
    results = []
    for value in sample_values:
        try:
            converted_value = convert_to_int(value)
            results.append(converted_value)
        except ConversionError as e:
            results.append(str(e))
    
    print(results)