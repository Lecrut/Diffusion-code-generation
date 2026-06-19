def convert_string_cases(input_string):
    lowercase = input_string.lower()
    uppercase = input_string.upper()
    titlecase = input_string.title()
    return lowercase, uppercase, titlecase

if __name__ == '__main__':
    sample_string = "Hello World"
    lower, upper, title = convert_string_cases(sample_string)
    print(lower)
    print(upper)
    print(title)