from typing import List

def snake_to_camel(text: str) -> str:
    words: List[str] = text.split("_")
    if not words:
        return ""
    first_word: str = words[0]
    camel_words: List[str] = [first_word.lower()]
    for word in words[1:]:
        if word:
            camel_words.append(word[0].upper() + word[1:].lower())
    return "".join(camel_words)

if __name__ == "__main__":
    sample_input: str = "hello_world_foo_bar"
    result: str = snake_to_camel(sample_input)
    print(result)