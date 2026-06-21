def parse_fixed_width_string(data_string: str, field_specs: list[tuple]) -> dict:
    if not data_string or not field_specs:
        raise ValueError("Input string and field specifications are required.")
    
    result = {}
    start_index = 0
    
    for field_name, length in field_specs:
        end_index = start_index + length
        if end_index > len(data_string):
            raise ValueError(f"Field '{field_name}' exceeds the length of the input string.")
        
        value = data_string[start_index:end_index].strip()
        result[field_name] = int(value) if value.isdigit() else value
        
        start_index = end_index
    
    return result

if __name__ == '__main__':
    sample_data = "10|apple|3.14|banana|20"
    field_specs = [("id", 2), ("name", 5), ("value", 6), ("description", 7), ("quantity", 2)]
    
    try:
        parsed_data = parse_fixed_width_string(sample_data, field_specs)
        print(f"Parsed Data: {parsed_data}")
    except ValueError as e:
        print(e)