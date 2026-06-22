from functools import reduce
import re

def snake_to_camel(text):
    parts = re.split(r'_+', text)
    return parts[0] + reduce(lambda acc, x: acc + x.capitalize(), parts[1:], '')

if __name__ == '__main__':
    sample_input = "this_is_a_test_string"
    result = snake_to_camel(sample_input)
    print(result)