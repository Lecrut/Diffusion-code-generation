def case_swap(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    def transform_case(s, method):
        return getattr(s, method)()
    
    methods = ['lower', 'upper', 'title']
    transformations = {method: transform_case(text, method) for method in methods}
    return transformations

if __name__ == '__main__':
    sample_text = "Hello World"
    result = case_swap(sample_text)
    print(result)

    another_sample = "Python Programming"
    another_result = case_swap(another_sample)
    print(another_result)