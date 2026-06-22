def validate_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def concatenate_strings(str1, str2):
    validate_string(str1)
    validate_string(str2)
    
    result = ""
    for char in str1:
        result += char
    for char in str2:
        result += char
    return result

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "World"
    concatenated_result = concatenate_strings(string1, string2)
    print(concatenated_result)