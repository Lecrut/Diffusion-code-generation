class ConversionError(Exception):
    pass
class InvalidSourceError(ConversionError):
    pass
class InvalidTargetError(ConversionError):
    pass
def convert_data(source_data, target_type):
    if not isinstance(source_data, list):
        raise InvalidSourceError("Source data must be a list.")
    if not isinstance(target_type, type):
        raise InvalidTargetError("Target type must be a Python type.")
    converted_list = []
    for item in source_data:
        if not isinstance(item, (int, float)):
            raise InvalidSourceError(f"Item {item} is not a valid number.")
        try:
            converted_value = target_type(item)
            converted_list.append(converted_value)
        except ValueError:
            raise ConversionError(f"Could not convert {item} to {target_type.__name__}.")
    return converted_list
if __name__ == '__main__':
    sample_source = [10, 25.5, 30, "error", 45.2]
    sample_target = int
    try:
        result = convert_data(sample_source, sample_target)
        print(result)
    except InvalidSourceError as e:
        print(f"Source Error: {e}")
    except InvalidTargetError as e:
        print(f"Target Error: {e}")
    except ConversionError as e:
        print(f"Conversion Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")