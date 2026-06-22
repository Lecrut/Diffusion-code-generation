from typing import List

def to_camel_case(text: str) -> str:
    if not text:
        return text
    
    parts: List[str] = text.split('_')
    if not parts:
        return ""
    
    first_part: str = parts[0].lower()
    camel_parts: List[str] = [first_part]
    
    for part in parts[1:]:
        if part:
            camel_parts.append(part.capitalize())
        else:
            camel_parts.append("")
    
    return "".join(camel_parts)

if __name__ == '__main__':
    sample_input_1: str = "hello_world_example"
    sample_input_2: str = "convert_this_string_to_camel_case"
    sample_input_3: str = "alreadyCamelCase"
    sample_input_4: str = "single_word"
    sample_input_5: str = ""
    
    result_1: str = to_camel_case(sample_input_1)
    result_2: str = to_camel_case(sample_input_2)
    result_3: str = to_camel_case(sample_input_3)
    result_4: str = to_camel_case(sample_input_4)
    result_5: str = to_camel_case(sample_input_5)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)