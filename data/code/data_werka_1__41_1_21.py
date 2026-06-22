def manipulate_case(input_string):
    case_operations = {
        "lowercase": str.lower,
        "uppercase": str.upper,
        "title_cased": str.title
    }
    
    result = {key: operation(input_string) for key, operation in case_operations.items()}
    return result

if __name__ == '__main__':
    sample_input = "Alibaba Cloud Example"
    result = manipulate_case(sample_input)
    print(result)