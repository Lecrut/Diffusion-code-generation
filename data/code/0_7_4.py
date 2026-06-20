class EmptyDigitResultException(Exception):
    def __init__(self, details):
        super().__init__(details)

def isolate_numeric_characters(source_text):
    numeric_parts = []
    for item in source_text:
        if item.isdigit():
            numeric_parts.append(item)
    return numeric_parts

def build_digit_string(data):
    extracted = isolate_numeric_characters(data)
    if not extracted:
        raise EmptyDigitResultException("Input lacks numeric content")
    merged = ""
    for char in extracted:
        merged += char
    return merged

if __name__ == '__main__':
    example_a = "test123abc45"
    example_b = "xyz"
    example_c = "007"
    output_a = build_digit_string(example_a)
    print(output_a)
    try:
        output_b = build_digit_string(example_b)
        print(output_b)
    except EmptyDigitResultException as err:
        print(str(err))
    output_c = build_digit_string(example_c)
    print(output_c)