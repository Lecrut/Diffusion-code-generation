def safe_strip(input_data):
    if input_data is None:
        return ""
    if not isinstance(input_data, str):
        converted = str(input_data)
        return converted.strip()
    return input_data.strip()

if __name__ == '__main__':
    sample_inputs = ["  hello  ", 42, None, "  world  \n", 3.14]
    for item in sample_inputs:
        result = safe_strip(item)
        print(result)