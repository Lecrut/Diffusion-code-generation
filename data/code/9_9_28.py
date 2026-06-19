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
            converted_value = convert_to_int(item)
            results.append(converted_value)
        except InvalidInputError as e:
            print(f"Invalid input encountered: {e}")
        except ConversionFailureError as e:
            print(f"Conversion failure encountered: {e}")
    return results

if __name__ == '__main__':
    sample_data = ['123', '456', 'abc', '789']
    conversion_results = process_conversion(sample_data)
    print(conversion_results)