import re

def to_camel_case(text: str) -> str:
    if not text:
        return ""
    parts = text.split("_")
    result_parts = [parts[0]]
    for part in parts[1:]:
        if part:
            result_parts.append(part.capitalize())
    return "".join(result_parts)

if __name__ == '__main__':
    sample_input = "hello_world_example"
    output = to_camel_case(sample_input)
    print(output)