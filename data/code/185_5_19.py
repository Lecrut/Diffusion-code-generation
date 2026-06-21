def parse_fixed_width_string(input_string):
    fields = {
        'name': (0, 20),
        'age': (20, 30),
        'email': (30, 50)
    }
    result = {}
    for field, indices in fields.items():
        start, end = indices
        result[field] = input_string[start:end].strip()
    return result

if __name__ == '__main__':
    sample_input = "John Doe         28 johndoe@example.com"
    print(parse_fixed_width_string(sample_input))