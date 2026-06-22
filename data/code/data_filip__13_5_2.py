import re
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)
if __name__ == '__main__':
    sample_inputs = ['hello_world', 'user_name', 'first_name_last_name']
    for s in sample_inputs:
        print(snake_to_camel(s))