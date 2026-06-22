def transform_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    upper_part = ''.join(c.upper() for c in s)
    lower_part = ''.join(c.lower() for c in s)
    
    return upper_part + lower_part

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    transformed_string = transform_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Transformed: {transformed_string}")