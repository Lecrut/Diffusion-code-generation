def manipulate_case(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    def transform_case(s, method):
        return getattr(s, method)()
    
    lowercase_str = transform_case(input_string, 'lower')
    uppercase_str = transform_case(input_string, 'upper')
    title_cased_str = transform_case(input_string, 'title')
    
    return {
        "lowercase": lowercase_str,
        "uppercase": uppercase_str,
        "title_cased": title_cased_str
    }

if __name__ == '__main__':
    sample_input = "Alibaba Cloud Example"
    try:
        result = manipulate_case(sample_input)
        print(result)
    except ValueError as e:
        print(e)