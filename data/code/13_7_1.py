def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def run_tests():
    test_cases = [
        ("hello_world", "helloWorld"),
        ("snake_case_to_camel_case", "snakeCaseToCamelCase"),
        ("single", "single"),
        ("multiple_words_here", "multipleWordsHere"),
        ("a_b_c", "aBC"),
    ]
    for input_val, expected in test_cases:
        result = to_camel_case(input_val)
        print(f"Input: {input_val}, Output: {result}, Expected: {expected}")
        if result != expected:
            raise ValueError(f"Test failed for {input_val}")

if __name__ == '__main__':
    run_tests()
    sample_input = "example_snake_case_string"
    print(to_camel_case(sample_input))