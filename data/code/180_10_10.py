SEARCH_WORD_SET = {"apple", "banana", "cherry"}

def is_word_present(word):
    return word.lower() in SEARCH_WORD_SET

if __name__ == '__main__':
    print(f"'apple' in search set: {is_word_present('Apple')}")
    print(f"'orange' in search set: {is_word_present('Orange')}")
    print(f"'banana' in search set: {is_word_present('Banana')}")