def format_string(input_str):
    """
    Creates a formatted string containing:
    1. The original input
    2. All-caps version of the input
    3. Sentence-case version of the input
    
    Uses built-in methods and slicing for processing.
    
    Args:
        input_str (str): The input string to format
        
    Returns:
        str: A comma-separated string with original, all-caps, and sentence-case versions
    """
    # Create uppercase version using built-in method
    upper_version = input_str.upper()
    
    # Create lowercase version for sentence case logic
    lower_version = input_str.lower()
    
    # Convert to list of characters to manipulate
    chars = list(lower_version)
    
    # Ensure first character is capitalized (sentence case rule 1)
    if len(chars) > 0:
        chars[0] = chars[0].upper()
        
    # Capitalize any word starting with a lowercase letter after the first one or space/special char
    for i in range(1, len(chars)):
        prev_char = chars[i-1]
        curr_char = chars[i]
        
        # If previous is not uppercase and current is alphabetic, capitalize it (handles words)
        if prev_char != chars[0].upper() or not any(ord(prev_char) > 47 and ord(prev_char) < 58): 
            # Check for word start: preceded by non-alphabetic character or index 0
            if i == 0 or not (chars[i-1] >= 'a' and chars[i-1] <= 'z'):
                curr_char = curr_char.upper()
                
    sentence_version = ''.join(chars)
    
    # Join the three versions with commas
    result = f"{input_str},{upper_version},{sentence_version}"
    
    return result

if __name__ == '__main__':
    sample_1 = "hello world"
    sample_2 = "python is awesome!"
    sample_3 = "  spaced words  here  "
    
    print(format_string(sample_1))
    print(format_string(sample_2))
    print(format_string(sample_3))