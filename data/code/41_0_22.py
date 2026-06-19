def convert_string_cases(input_string):
    lower_case = input_string.lower()
    upper_case = input_string.upper()
    title_case = input_string.title()
    return lower_case, upper_case, title_case

if __name__ == '__main__':
    sample_string = "Hello World"
    lower, upper, title = convert_string_cases(sample_string)
    print(lower)
    print(upper)
    print(title)