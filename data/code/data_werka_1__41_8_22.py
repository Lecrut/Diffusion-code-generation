def case_swap(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    def to_lower(s):
        return s.lower()
    
    def to_upper(s):
        return s.upper()
    
    def to_title(s):
        return s.title()
    
    return {
        'lower': to_lower(text),
        'upper': to_upper(text),
        'title': to_title(text)
    }

if __name__ == '__main__':
    sample_text = "Hello World"
    result = case_swap(sample_text)
    print(result)