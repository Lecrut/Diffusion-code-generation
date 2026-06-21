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
    try:
        return int(value)
    except ValueError as e:
        raise InvalidInputError(value) from e
    except Exception as e:
        raise ConversionFailedError(value) from e

if __name__ == '__main__':
    sample_values = ['123', 'abc', '456.78', '-90']
    results = []
    for value in sample_values:
        try:
            result = convert_to_int(value)
            results.append(result)
        except InvalidInputError as e:
            print(e)
        except ConversionFailedError as e:
            print(e)
    print(results)