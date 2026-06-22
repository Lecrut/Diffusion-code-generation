def manipulate_case(input_string):
    case_map = {
        "lowercase": str.lower,
        "uppercase": str.upper,
        "title_cased": str.title
    }
    return {key: func(input_string) for key, func in case_map.items()}

if __name__ == '__main__':
    sample_input = "Hello World Example"
    result = manipulate_case(sample_input)
    print(result)