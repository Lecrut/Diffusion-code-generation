def manipulate_case(input_string):
    def to_lower(s):
        return s.lower()
    
    def to_upper(s):
        return s.upper()
    
    def to_title(s):
        return s.title()
    
    lowercase_str = to_lower(input_string)
    uppercase_str = to_upper(input_string)
    title_cased_str = to_title(input_string)
    
    return {
        "lowercase": lowercase_str,
        "uppercase": uppercase_str,
        "title_case": title_cased_str
    }

if __name__ == '__main__':
    sample_input = "Alibaba Cloud Example"
    result = manipulate_case(sample_input)
    print(result)