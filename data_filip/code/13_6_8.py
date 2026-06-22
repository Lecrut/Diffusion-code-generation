from typing import Final

def snake_to_camel(snake_case: str) -> str:
    if not snake_case:
        return ""
    if snake_case.startswith('_'):
        return "_" + snake_to_camel(snake_case[1:])
    if snake_case.endswith('_'):
        return snake_to_camel(snake_case[:-1]) + "_"
    
    parts: list[str] = snake_case.split('_')
    result: list[str] = []
    
    for i, part in enumerate(parts):
        if not part:
            result.append('_')
        else:
            if i == 0:
                result.append(part.lower())
            else:
                result.append(part.capitalize())
    
    return "".join(result)

if __name__ == '__main__':
    sample_inputs: list[str] = ["hello_world", "my_variable_name", "snake_case_to_camel_case", "alreadyCamelCase", "single"]
    for input_str in sample_inputs:
        converted: str = snake_to_camel(input_str)
        print(f"{input_str} -> {converted}")