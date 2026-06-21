def snake_to_camel(snake_case):
    parts = snake_case.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = ['hello_world', 'user_profile_data', 'snake_case_to_camel_case', 'alreadyCamel', 'single']
    for case in test_cases:
        print(snake_to_camel(case))