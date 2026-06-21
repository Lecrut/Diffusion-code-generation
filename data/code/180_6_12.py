def check_word_presence(word_list: list[str], target_word: str) -> bool:
    word_set = set(word_list)
    return target_word in word_set

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'date']
    print(f"Test 1 (Present): {check_word_presence(sample_words, 'banana')}")
    print(f"Test 2 (Absent): {check_word_presence(sample_words, 'grape')}")