def manipulate_case(text: str, case_type: str = 'lower') -> str:
    if case_type == 'lower':
        return text.lower()
    elif case_type == 'upper':
        return text.upper()
    elif case_type == 'title':
        return text.title()
    elif case_type == 'swap':
        return text.swapcase()
    else:
        return text

if __name__ == '__main__':
    original_string = "Hello World"
    lower_result = manipulate_case(original_string, 'lower')
    print(lower_result)
    upper_result = manipulate_case(original_string, 'upper')
    print(upper_result)
    title_result = manipulate_case(original_string, 'title')
    print(title_result)
    swap_result = manipulate_case(original_string, 'swap')
    print(swap_result)
    invalid_result = manipulate_case(original_string, 'invalid')
    print(invalid_result)