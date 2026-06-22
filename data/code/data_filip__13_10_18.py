import re

def snake_to_camel(text):
    def replace(match):
        return match.group(1).upper()
    return re.sub(r'_([a-z])', replace, text)

if __name__ == '__main__':
    sample_data = ["hello_world", "this_is_a_test_string", "snake_case_example"]
    for s in sample_data:
        print(snake_to_camel(s))