import re

def snake_to_camel(text: str) -> str:
    def replace_func(match: re.Match) -> str:
        return match.group(0).replace('_', '').upper()
    return re.sub(r'_([a-zA-Z])', replace_func, text)

if __name__ == '__main__':
    result = snake_to_camel("hello_world_test_string")
    print(result)