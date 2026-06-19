def transform_string(s):
    upper_chars = {chr(i): chr(i).upper() for i in range(97, 123)}
    lower_chars = {chr(i): chr(i).lower() for i in range(65, 91)}

    uppercase_result = ''.join(upper_chars.get(char, char) for char in s)
    lowercase_result = ''.join(lower_chars.get(char, char) for char in s)

    return uppercase_result, lowercase_result

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    upper, lower = transform_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Uppercase: {upper}")
    print(f"Lowercase: {lower}")