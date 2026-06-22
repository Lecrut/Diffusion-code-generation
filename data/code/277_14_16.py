MAX_WORD_LENGTH = 10

def count_words(text):
    word_count = 0
    current_word = ""
    for char in text:
        if char.isalpha():
            current_word += char
        elif len(current_word) > 0:
            word_count += 1
            if len(current_word) > MAX_WORD_LENGTH:
                print(f"Warning: Word '{current_word}' exceeds maximum length of {MAX_WORD_LENGTH}")
            current_word = ""
    if len(current_word) > 0:
        word_count += 1
        if len(current_word) > MAX_WORD_LENGTH:
            print(f"Warning: Word '{current_word}' exceeds maximum length of {MAX_WORD_LENGTH}")
    return word_count

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(count_words(sample_text))