def snake_to_camel(text: str) -> str:
    if not text:
        return ""
    words = text.split('_')
    if not words:
        return ""
    result_words = [words[0]]
    for word in words[1:]:
        if word:
            result_words.append(word.capitalize())
    return ''.join(result_words)

if __name__ == '__main__':
    sample_input = "hello_world_name"
    result = snake_to_camel(sample_input)
    print(result)