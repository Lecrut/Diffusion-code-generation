class ConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidInputError(ConversionError):
    def __init__(self, value):
        super().__init__(f"Invalid input: {value} cannot be converted to an integer.")

class ConversionFailureError(ConversionError):
    def __init__(self, value, reason):
        super().__init__(f"Conversion failure for {value}: {reason}")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise InvalidInputError(value) from e
    except Exception as e:
        raise ConversionFailureError(value, str(e))

def process_conversion(data):
    results = []
    for item in data:
        try:
            converted_value = convert_to_int(item)
            results.append(converted_value)
        except ConversionError as e:
            print(f"Error processing {item}: {e}")
    return results

if __name__ == '__main__':
    sample_data = ['123', '456', 'abc', '789']
    converted_values = process_conversion(sample_data)
    print(converted_values)