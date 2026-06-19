def transform_string(s):
    upper_chars = [chr(c) for c in range(65, 91)]
    lower_chars = [chr(c) for c in range(97, 123)]
    
    char_map = {upper: lower for upper, lower in zip(upper_chars, lower_chars)}
    
    uppercase = ''.join(char_map.get(c, c) if c in char_map else c.upper() for c in s)
    lowercase = ''.join(char_map.get(c.lower(), c.lower()) for c in s)
    
    return uppercase, lowercase

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    upper_result, lower_result = transform_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Uppercase: {upper_result}")
    print(f"Lowercase: {lower_result}")