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
def get_required_data(data_dict, required_fields):
    result = {}
    for field, required_type in required_fields.items():
        if field in data_dict:
            value = data_dict[field]
            if required_type == int:
                if get_integer_input(f"Enter {field}: ", value) is not None:
                    result[field] = get_integer_input(f"Enter {field}: ", value)
                else:
                    return None
            elif required_type == str:
                if get_string_input(f"Enter {field}: ", value) is not None:
                    result[field] = get_string_input(f"Enter {field}: ", value)
                else:
                    return None
            elif required_type == float:
                if get_float_input(f"Enter {field}: ", value) is not None:
                    result[field] = get_float_input(f"Enter {field}: ", value)
                else:
                    return None
        else:
            return None
    return result
if __name__ == '__main__':
    sample_data = {
        "age": "25",
        "name": "Alice",
        "score": "95.5"
    }
    required_fields = {
        "age": int,
        "name": str,
        "score": float
    }
    print("--- Testing successful input ---")
    result_success = get_required_data(sample_data, required_fields)
    print(result_success)
    print("\n--- Testing missing required field (name) ---")
    sample_data_missing = {
        "age": "30",
        "score": "88.0"
    }
    result_missing = get_required_data(sample_data_missing, required_fields)
    print(result_missing)
    print("\n--- Testing invalid data type (age) ---")
    sample_data_invalid = {
        "age": "twenty",
        "name": "Bob",
        "score": "90.0"
    }
    result_invalid = get_required_data(sample_data_invalid, required_fields)
    print(result_invalid)
    print("\n--- Testing invalid data type (score) ---")
    sample_data_invalid_2 = {
        "age": "22",
        "name": "Charlie",
        "score": "ninety"
    }
    result_invalid_2 = get_required_data(sample_data_invalid_2, required_fields)
    print(result_invalid_2)