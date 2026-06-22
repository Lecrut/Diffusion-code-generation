def transform_text(input_string):
    lower_case = input_string.lower()
    upper_case = input_string.upper()
    title_case = input_string.title()
    return lower_case, upper_case, title_case

if __name__ == '__main__':
    test_string = "Python Programming Is Fun!"
    lowercase_result, uppercase_result, titlecase_result = transform_text(test_string)
    print(f"Original: {test_string}")
    print(f"Lowercase: {lowercase_result}")
    print(f"Uppercase: {uppercase_result}")
    print(f"Title Case: {titlecase_result}")