class ConversionError(Exception):
    pass
class InvalidSourceError(ConversionError):
    pass
class InvalidTargetError(ConversionError):
    pass
def convert_data(source_value, target_type):
    if not isinstance(source_value, (int, float)):
        raise InvalidSourceError(f"Source value '{source_value}' is not a valid number.")
    if target_type == 'int':
        if source_value != int(source_value):
            raise ConversionError(f"Cannot convert {source_value} to integer without loss of precision.")
        return int(source_value)
    elif target_type == 'float':
        return float(source_value)
    else:
        raise InvalidTargetError(f"Unsupported target type: {target_type}")
if __name__ == '__main__':
    sample_source = 10.5
    sample_target = 'float'
    try:
        result = convert_data(sample_source, sample_target)
        print(f"Conversion successful. Result: {result}")
    except InvalidSourceError as e:
        print(f"Source Error: {e}")
    except InvalidTargetError as e:
        print(f"Target Error: {e}")
    except ConversionError as e:
        print(f"Conversion Logic Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 20)
    sample_source_invalid = "abc"
    sample_target_invalid = 'int'
    try:
        result = convert_data(sample_source_invalid, sample_target_invalid)
        print(f"Conversion successful. Result: {result}")
    except InvalidSourceError as e:
        print(f"Source Error: {e}")
    except InvalidTargetError as e:
        print(f"Target Error: {e}")
    except ConversionError as e:
        print(f"Conversion Logic Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")