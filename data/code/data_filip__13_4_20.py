import re

def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_data = [
        "user_name",
        "first_name_and_last_name",
        "simple",
        "multiple_words_here_test_case",
        "a_b_c_d_e"
    ]
    
    for data in sample_data:
        result = snake_to_camel(data)
        print(f"{data} -> {result}")