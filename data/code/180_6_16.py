TARGET_WORDS = {'apple', 'banana', 'cherry'}

def check_word_presence(word: str) -> bool:
    return word in TARGET_WORDS

if __name__ == '__main__':
    print(f"Test 1 (Present): {check_word_presence('banana')}")
    print(f"Test 2 (Absent): {check_word_presence('orange')}")