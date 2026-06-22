from typing import List

def snake_to_camel(snake_string: str) -> str:
    words: List[str] = snake_string.split("_")
    if not words:
        return ""
    
    first_word: str = words[0]
    rest_words: List[str] = words[1:]
    
    capitalized_rest: List[str] = [word.capitalize() for word in rest_words]
    
    result_parts: List[str] = [first_word] + capitalized_rest
    return "".join(result_parts)

if __name__ == '__main__':
    test_input: str = "hello_world_foo_bar"
    result: str = snake_to_camel(test_input)
    print(result)