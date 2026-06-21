def create_word_set(words: list[str]) -> set[str]:
    return set(words)

def check_word_presence(word_set: set[str], word: str) -> bool:
    if not isinstance(word, str):
        raise ValueError("Word must be a string")
    return word in word_set

if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry']
    word_set = create_word_set(words)
    print(f"Test 1 (Present): {check_word_presence(word_set, 'banana')}")
    print(f"Test 2 (Absent): {check_word_presence(word_set, 'orange')}")