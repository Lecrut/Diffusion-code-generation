def match_dictionary_to_keys(data_dict, allowed_keys):
    matched_data = {}
    for key, value in data_dict.items():
        if key in allowed_keys:
            matched_data[key] = value
        else:
            matched_data[key] = "unmatched"
    return matched_data
if __name__ == '__main__':
    sample_data = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer"
    }
    allowed_keys = ["name", "age", "city", "email"]
    try:
        result = match_dictionary_to_keys(sample_data, allowed_keys)
        print(result)
    except TypeError as e:
        print(f"Error during execution: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    invalid_data = {
        "name": "Bob",
        "phone": "1234567890"
    }
    try:
        result_invalid = match_dictionary_to_keys(invalid_data, allowed_keys)
        print("\nTesting invalid data:")
        print(result_invalid)
    except TypeError as e:
        print(f"Error during execution for invalid data: {e}")