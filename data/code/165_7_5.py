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
        else:
            return None
    return result
if __name__ == '__main__':
    sample_data = {
        "age": "30",
        "name": "Alice"
    }
    required_fields = {
        "age": int,
        "name": str
    }
    print("--- Test Case 1: Valid Data ---")
    result1 = get_required_data(sample_data, required_fields)
    print(f"Result 1: {result1}")
    print("\n--- Test Case 2: Invalid Type (Age) ---")
    invalid_data_1 = {
        "age": "thirty",
        "name": "Bob"
    }
    result2 = get_required_data(invalid_data_1, required_fields)
    print(f"Result 2: {result2}")
    print("\n--- Test Case 3: Missing Field (Name) ---")
    missing_data_2 = {
        "age": "25"
    }
    result3 = get_required_data(missing_data_2, required_fields)
    print(f"Result 3: {result3}")
    print("\n--- Test Case 4: Invalid Type and Missing Field ---")
    invalid_data_3 = {
        "age": 40,
        "name": 12345
    }
    result4 = get_required_data(invalid_data_3, required_fields)
    print(f"Result 4: {result4}")