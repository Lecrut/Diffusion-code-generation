def manipulate_case(input_string):
    lowercase_version = input_string.lower()
    uppercase_version = input_string.upper()
    title_cased_version = input_string.title()
    return {
        "lowercase": lowercase_version,
        "uppercase": uppercase_version,
        "title_cased": title_cased_version
    }

if __name__ == '__main__':
    sample_text = "Python Programming"
    case_manipulated_result = manipulate_case(sample_text)
    print(case_manipulated_result)