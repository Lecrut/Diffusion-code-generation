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
def get_required_input(prompt, sample_value):
    if sample_value is None:
        return None
    return sample_value
def process_data(num_input, name_input):
    if num_input is None or name_input is None:
        return "Error: Missing required input."
    try:
        number = int(num_input)
        name = str(name_input)
        if number <= 0:
            return "Error: Number must be positive."
        return f"Success: Number is {number} and Name is {name}."
    except ValueError:
        return "Error: Invalid data type entered for number."
if __name__ == '__main__':
    sample_num = "100"
    sample_name = "Alice"
    num_result = get_integer_input("Enter number", sample_num)
    name_result = get_string_input("Enter name", sample_name)
    required_num = get_required_input("Number", num_result)
    required_name = get_required_input("Name", name_result)
    result = process_data(required_num, required_name)
    print(result)
    sample_num_invalid = "abc"
    sample_name_missing = None
    num_result_invalid = get_integer_input("Enter number", sample_num_invalid)
    name_result_invalid = get_string_input("Enter name", sample_name_missing)
    required_num_invalid = get_required_input("Number", num_result_invalid)
    required_name_invalid = get_required_input("Name", name_result_invalid)
    result_invalid = process_data(required_num_invalid, required_name_invalid)
    print(result_invalid)