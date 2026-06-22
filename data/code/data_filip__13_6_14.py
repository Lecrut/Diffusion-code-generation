from typing import List

def snake_to_camel(s: str) -> str:
    parts: List[str] = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

if __name__ == "__main__":
    result: str = snake_to_camel("my_variable_name")
    print(result)