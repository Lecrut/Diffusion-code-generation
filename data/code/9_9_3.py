class ConversionError(Exception):
    pass
class InvalidSourceError(ConversionError):
    pass
class InvalidTargetError(ConversionError):
    pass
def convert_data(source_data, target_type):
    if not isinstance(source_data, (list, dict)):
        raise InvalidSourceError("Source data must be a list or a dictionary.")
    if target_type == "int":
        if not all(isinstance(item, int) for item in source_data):
            raise InvalidTargetError("All source items must be convertible to integers.")
        return [item for item in source_data]
    elif target_type == "str":
        if not all(isinstance(item, str) for item in source_data):
            raise InvalidTargetError("All source items must be strings.")
        return [str(item) for item in source_data]
    else:
        raise ConversionError(f"Unsupported target type: {target_type}")
if __name__ == '__main__':
    sample_source_int = [1, 2, 3, 4]
    sample_source_str = ["a", "b", "c", "d"]
    sample_source_mixed = [1, "two", 3]
    sample_target_int = "int"
    sample_target_str = "str"
    sample_target_invalid = "float"
    try:
        result_int = convert_data(sample_source_int, sample_target_int)
        print(f"Converted to int: {result_int}")
        result_str = convert_data(sample_source_str, sample_target_str)
        print(f"Converted to str: {result_str}")
        convert_data(sample_source_mixed, sample_target_int)
    except InvalidSourceError as e:
        print(f"Source Error: {e}")
    except InvalidTargetError as e:
        print(f"Target Error: {e}")
    except ConversionError as e:
        print(f"Conversion Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")