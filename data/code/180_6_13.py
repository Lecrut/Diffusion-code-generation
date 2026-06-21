def validate_word_presence(text: str | None, word: str) -> bool:
    if text is None or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string")
    if not word:
        raise ValueError("Word cannot be empty")
    return word in text

if __name__ == '__main__':
    try:
        print(f"Test 1 (Present): {validate_word_presence('hello world', 'world')}")
        print(f"Test 2 (Absent): {validate_word_presence('hello world', 'python')}")
        print(f"Test 3 (Empty Text): {validate_word_presence('', 'test')}")
        print(f"Test 4 (None Text): {validate_word_presence(None, 'test')}")
        print(f"Test 5 (Empty Word): {validate_word_presence('some text', '')}")
        print(f"Test 6 (Empty Word with None Text): {validate_word_presence(None, '')}")
        print(f"Test 7 (Word in Empty Text): {validate_word_presence('', 'test')}")
    except ValueError as e:
        print(e)