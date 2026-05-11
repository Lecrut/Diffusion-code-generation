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
    except Exception:
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
    if not isinstance(data, (int, float, str)):
        return False, "Invalid data type provided"
    return True, "Data successfully processed"
if __name__ == '__main__':
    sample_int = "100"
    sample_string = "hello"
    sample_float = "3.14"
    sample_invalid_int = "abc"
    sample_missing = None
    int_result = get_integer_input("Enter integer:", sample_int)
    string_result = get_string_input("Enter string:", sample_string)
    float_result = get_float_input("Enter float:", sample_float)
    print(f"Integer Result: {int_result}")
    print(f"String Result: {string_result}")
    print(f"Float Result: {float_result}")
    print("-" * 20)
    validate_and_process_data(int_result)
    validate_and_process_data(string_result)
    validate_and_process_data(float_result)
    validate_and_process_data(sample_missing)
    validate_and_process_data("not_a_number")