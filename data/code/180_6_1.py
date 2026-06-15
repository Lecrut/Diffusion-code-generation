def check_word_presence(text: str | None, word: str) -> bool:
    if text is None or not isinstance(text, str):
        return False
    if not word:
        return False
    return word in text.lower()
if __name__ == '__main__':
    print(f"Test 1 (Present): {check_word_presence('Hello world', 'world')}")
    print(f"Test 2 (Absent): {check_word_presence('Hello world', 'python')}")
    print(f"Test 3 (Case Insensitive): {check_word_presence('Hello World', 'world')}")
    print(f"Test 4 (Empty Text): {check_word_presence('', 'test')}")
    print(f"Test 5 (None Text): {check_word_presence(None, 'test')}")
    print(f"Test 6 (Empty Word): {check_word_presence('some text', '')}")
    print(f"Test 7 (Empty Word with None Text): {check_word_presence(None, '')}")
    print(f"Test 8 (Word in Empty Text): {check_word_presence('', 'test')}")