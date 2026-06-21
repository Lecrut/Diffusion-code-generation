def reverse_word_order(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_string = "Python is awesome"
    result = reverse_word_order(sample_string)
    print(f"'{sample_string}' -> '{result}'")