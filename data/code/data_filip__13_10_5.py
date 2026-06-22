import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)

if __name__ == '__main__':
    sample_input_1 = "hello_world_example"
    sample_input_2 = "this_is_a_test_string"
    sample_input_3 = "single"
    sample_input_4 = "alreadyCamelCase"
    
    result_1 = snake_to_camel(sample_input_1)
    result_2 = snake_to_camel(sample_input_2)
    result_3 = snake_to_camel(sample_input_3)
    result_4 = snake_to_camel(sample_input_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)