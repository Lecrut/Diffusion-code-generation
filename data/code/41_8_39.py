def case_swap(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    def transform_case(s, method):
        return getattr(s, method)()
    
    return {
        'lower': transform_case(text, 'lower'),
        'upper': transform_case(text, 'upper'),
        'title': transform_case(text, 'title')
    }

if __name__ == '__main__':
    sample_text = "Sample Text"
    result = case_swap(sample_text)
    print(result)