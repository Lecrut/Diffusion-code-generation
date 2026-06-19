def manipulate_case(input_string):
    lowercased = input_string.lower()
    uppercased = input_string.upper()
    title_cased = input_string.title()
    
    return {
        "lowercase": lowercased,
        "uppercase": uppercased,
        "title_case": title_cased
    }

if __name__ == '__main__':
    test_input = "Python Programming"
    case_manipulated = manipulate_case(test_input)
    print(case_manipulated)