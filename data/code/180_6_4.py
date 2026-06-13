def check_word_presence(text: str | None, word: str) -> bool:
    if not text or not word:
        return False
    return word in text.lower()
if __name__ == '__main__':
    print(check_word_presence("Hello world", "world"))
    print(check_word_presence("", "test"))
    print(check_word_presence(None, "test"))
    print(check_word_presence("Programming is fun", "fun"))
    print(check_word_presence("Python", "java"))
    print(check_word_presence("Apple Banana Cherry", "apple"))