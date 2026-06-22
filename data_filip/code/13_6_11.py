from typing import List

def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ""
    parts: List[str] = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    first_part: str = parts[0]
    capitalized_parts: List[str] = [part.capitalize() for part in parts[1:]]
    result: str = first_part + ''.join(capitalized_parts)
    return result

if __name__ == '__main__':
    sample_input_1: str = "hello_world"
    sample_input_2: str = "convert_this_string_to_camel_case"
    sample_input_3: str = "singleword"
    sample_input_4: str = "multiple___underscores"
    print(snake_to_camel(sample_input_1))
    print(snake_to_camel(sample_input_2))
    print(snake_to_camel(sample_input_3))
    print(snake_to_camel(sample_input_4))