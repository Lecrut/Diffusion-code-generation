class ConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidInputError(ConversionError):
    def __init__(self, message):
        super().__init__(f"Invalid input: {message}")

class ConversionFailureError(ConversionError):
    def __init__(self, message):
        super().__init__(f"Conversion failure: {message}")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise InvalidInputError(f"{value} cannot be converted to an integer.") from e
    except Exception as e:
        raise ConversionFailureError(f"Failed to convert {value} to integer") from e

def process_conversion(data):
    results = []
    for item in data:
        try:
            result = convert_to_int(item)
            results.append(result)
        except InvalidInputError as e:
            print(e)
        except ConversionFailureError as e:
            print(e)
    return results

if __name__ == '__main__':
    sample_data = ['123', 'abc', '456', None, '789']
    conversion_results = process_conversion(sample_data)
    print(conversion_results)