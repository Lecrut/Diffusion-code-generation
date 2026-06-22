def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def manipulate_case(input_string):
    validate_input(input_string)
    
    lowercase_str = input_string.lower()
    uppercase_str = input_string.upper()
    title_cased_str = input_string.title()
    
    return {
        "lowercase": lowercase_str,
        "uppercase": uppercase_str,
        "title_cased": title_cased_str
    }

if __name__ == '__main__':
    sample_input = "Alibaba Cloud Example"
    result = manipulate_case(sample_input)
    print(result)