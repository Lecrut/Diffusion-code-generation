def manipulate_case(input_string):
    lowercase_str = input_string.lower()
    uppercase_str = input_string.upper()
    title_cased_str = str(input_string).title()
    return {
        "lowercase": lowercase_str,
        "uppercase": uppercase_str,
        "title_case": title_cased_str
    }
if __name__ == '__main__':
    sample = "Hello World Example"
    result = manipulate_case(sample)
    print(result)