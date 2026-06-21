class WordPresenceChecker:
    @staticmethod
    def check_word_presence(text: str | None, word: str) -> bool:
        if text is None or not isinstance(text, str):
            return False
        if not word:
            return False
        return word in text

if __name__ == '__main__':
    checker = WordPresenceChecker()
    print(f"Test 1 (Present): {checker.check_word_presence('hello world', 'world')}")
    print(f"Test 2 (Absent): {checker.check_word_presence('hello world', 'python')}")
    print(f"Test 3 (Empty Text): {checker.check_word_presence('', 'test')}")
    print(f"Test 4 (None Text): {checker.check_word_presence(None, 'test')}")
    print(f"Test 5 (Empty Word): {checker.check_word_presence('some text', '')}")
    print(f"Test 6 (Empty Word with None Text): {checker.check_word_presence(None, '')}")
    print(f"Test 7 (Word in Empty Text): {checker.check_word_presence('', 'test')}")