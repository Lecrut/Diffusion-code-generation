import re
def split_words_pythically(text: str) -> list[str]:
    return [word for word in text.split() if len(word.strip()) > 0]
if __name__ == '__main__':
    sample_text = "Hello, World! This is Python.\nIt's very powerful."
    words = split_words_pythically(sample_text)
    print("Split result:", words)
    assert isinstance(words, list), "Result must be a list"
    for word in words:
        if not isinstance(word, str):
            raise AssertionError(f"All elements should be strings")
    exit_code = 0