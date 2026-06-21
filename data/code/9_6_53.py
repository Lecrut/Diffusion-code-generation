class ConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidInputError(ConversionError):
    def __init__(self, value):
        super().__init__(f'Invalid input: {value}')

class ConversionFailedError(ConversionError):
    def __init__(self, value):
        super().__init__(f'Conversion failed for value: {value}')

def convert_to_int(value):
    if not isinstance(value, str):
        raise InvalidInputError(f'Non-string input provided: {value}')
    try:
        return int(value)
    except ValueError as e:
        raise ConversionFailedError(value) from e

def safe_conversion(values):
    results = []
    for value in values:
        try:
            converted_value = convert_to_int(value)
            results.append(converted_value)
        except (InvalidInputError, ConversionFailedError) as e:
            print(e)
    return results

if __name__ == '__main__':
    sample_values = ['123', 'abc', '456.78', '-90']
    conversion_results = safe_conversion(sample_values)
    for result in conversion_results:
        print(result)