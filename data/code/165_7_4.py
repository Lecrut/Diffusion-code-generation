def get_integer_input(prompt, sample_value):
    try:
        value = int(sample_value)
        return value
    except ValueError:
        return None
def get_string_input(prompt, sample_value):
    try:
        value = str(sample_value)
        return value
    except ValueError:
        return None
def get_float_input(prompt, sample_value):
    try:
        value = float(sample_value)
        return value
    except ValueError:
        return None
def validate_and_process_data(data):
    if data is None:
        return False, "Missing required data"
    if not data:
        return False, "Input cannot be empty"
    return True, "Data successfully processed"
if __name__ == '__main__':
    sample_int = "100"
    sample_string = "hello"
    sample_float = "3.14"
    int_result = get_integer_input("Enter integer:", sample_int)
    string_result = get_string_input("Enter string:", sample_string)
    float_result = get_float_input("Enter float:", sample_float)
    print(f"Integer result: {int_result}")
    print(f"String result: {string_result}")
    print(f"Float result: {float_result}")
    data_to_validate = [int_result, string_result, float_result]
    is_valid, message = validate_and_process_data(data_to_validate)
    print(f"Validation Status: {is_valid}")
    print(f"Message: {message}")