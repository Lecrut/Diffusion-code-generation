import re

def snake_to_camel(text: str) -> str:
    if not text:
        return text
    
    def replace(match):
        return match.group(2).upper()
    
    pattern = re.compile(r'(_)([a-zA-Z])')
    return pattern.sub(replace, text)

if __name__ == '__main__':
    sample_input = "this_is_a_snake_case_string"
    result = snake_to_camel(sample_input)
    print(result)