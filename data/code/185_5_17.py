def parse_fixed_width_string(data_string: str) -> dict:
    start_indices = [0, 5, 10, 15]
    end_indices = [4, 9, 14, len(data_string)]
    field_names = ['field1', 'field2', 'field3', 'field4']
    result = {}
    
    for name, start, end in zip(field_names, start_indices, end_indices):
        value = data_string[start:end].strip()
        if value.isdigit():
            result[name] = int(value)
        else:
            result[name] = value
    
    return result

if __name__ == '__main__':
    sample_data = "12345hello67890world"
    parsed_data = parse_fixed_width_string(sample_data)
    print(f"Input String: {sample_data}")
    print("Parsed Data:")
    for key, value in parsed_data.items():
        print(f"{key}: {value}")