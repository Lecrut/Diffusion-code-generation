from typing import Text

def snake_to_camel(text: Text) -> Text:
    parts = text.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

if __name__ == "__main__":
    result: str = snake_to_camel("hello_world_example")
    print(result)