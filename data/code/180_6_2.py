def check_word_presence(text: str | None, word: str) -> bool:
    if not isinstance(text, str):
        return False
    if not text:
        return False
    return word in text
if __name__ == '__main__':
    print(f"Test 1 (Present): {check_word_presence('hello world', 'world')}")
    print(f"Test 2 (Absent): {check_word_presence('hello world', 'python')}")
    print(f"Test 3 (Empty Text): {check_word_presence('', 'test')}")
    print(f"Test 4 (None Text): {check_word_presence(None, 'test')}")
    print(f"Test 5 (Empty Word): {check_word_presence('test', '')}")
    print(f"Test 6 (Case Sensitivity): {check_word_presence('Hello world', 'world')}")