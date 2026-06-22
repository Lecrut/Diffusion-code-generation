def concatenate_strings(str1, str2):
    result = ""
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    for char in str1:
        result += char
    for char in str2:
        result += char
    
    return result

if __name__ == '__main__':
    sample_string1 = "Hello"
    sample_string2 = "World"
    concatenated_result = concatenate_strings(sample_string1, sample_string2)
    print(concatenated_result)