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
def process_data(int_val, str_val, float_val):
    if int_val is None or str_val is None or float_val is None:
        return "Error: Missing or invalid data provided."
    return f"Successfully processed: Integer={int_val}, String='{str_val}', Float={float_val}"
if __name__ == '__main__':
    sample_int = "100"
    sample_str = "hello"
    sample_float = "3.14"
    int_result = get_integer_input("Enter integer:", sample_int)
    str_result = get_string_input("Enter string:", sample_str)
    float_result = get_float_input("Enter float:", sample_float)
    result = process_data(int_result, str_result, float_result)
    print(result)
    print("-" * 20)
    invalid_int = "abc"
    invalid_str = "xyz"
    invalid_float = "not_a_number"
    int_result_err = get_integer_input("Enter integer:", invalid_int)
    str_result_err = get_string_input("Enter string:", invalid_str)
    float_result_err = get_float_input("Enter float:", invalid_float)
    result_err = process_data(int_result_err, str_result_err, float_result_err)
    print(result_err)