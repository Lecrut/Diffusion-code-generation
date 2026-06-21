def check_word_presence(words: list[str], target: str) -> bool:
    if not words or not target:
        return False
    word_set = set(words)
    return target in word_set

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry']
    target_word = 'banana'
    print(f"Test 1 (Present): {check_word_presence(sample_words, target_word)}")
    
    target_word = 'grape'
    print(f"Test 2 (Absent): {check_word_presence(sample_words, target_word)}")
    
    sample_words = []
    target_word = 'apple'
    print(f"Test 3 (Empty List): {check_word_presence(sample_words, target_word)}")
    
    sample_words = ['apple', 'banana']
    target_word = ''
    print(f"Test 4 (Empty Target Word): {check_word_presence(sample_words, target_word)}")