def parse_fixed_width_string(input_str):
    fields = {
        'name': (0, 20),
        'age': (20, 25),
        'email': (25, 65)
    }
    result = {}
    for field, indices in fields.items():
        start, end = indices
        result[field] = input_str[start:end].strip()
    return result

if __name__ == '__main__':
    sample_input = "John Doe     30john.doe@example.com"
    print(parse_fixed_width_string(sample_input))