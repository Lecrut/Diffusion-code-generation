from typing import List

def to_camel_case(text: str) -> str:
    if not text:
        return ""
    
    parts: List[str] = text.split("_")
    if not parts:
        return ""
    
    first_word: str = parts[0]
    camel_parts: List[str] = [first_word]
    
    for part in parts[1:]:
        if part:
            camel_parts.append(part[0].upper() + part[1:])
    
    return "".join(camel_parts)

if __name__ == '__main__':
    sample_input: str = "convert_snake_case_to_camel_case"
    result: str = to_camel_case(sample_input)
    print(result)