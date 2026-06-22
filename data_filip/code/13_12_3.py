import sys

def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    
    parts = snake_str.split('_')
    if not parts:
        return ''
    
    camel_parts = [parts[0]]
    for part in parts[1:]:
        if part:
            camel_parts.append(part[0].upper() + part[1:])
    
    return ''.join(camel_parts)

if __name__ == '__main__':
    sample_snake = "hello_world_example_string"
    result = snake_to_camel(sample_snake)
    print(result)