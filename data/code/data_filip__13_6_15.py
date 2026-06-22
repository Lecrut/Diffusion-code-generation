from typing import List

def snake_to_camel(input_string: str) -> str:
    if not input_string:
        return ""
    
    parts: List[str] = input_string.split('_')
    
    if len(parts) == 1:
        return parts[0]
    
    camel_parts: List[str] = [parts[0].lower()]
    
    for part in parts[1:]:
        if not part:
            continue
        camel_parts.append(part.capitalize())
    
    return ''.join(camel_parts)

if __name__ == '__main__':
    sample_input: str = "this_is_a_test_string"
    result: str = snake_to_camel(sample_input)
    print(result)