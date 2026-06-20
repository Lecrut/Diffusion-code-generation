SPECIAL_CHARS = set("!@#$%^&*()_+-=[]{}|;':\",./<>?\\`~")

def contains_special_characters(text: str) -> bool:
    char_set = set(text)
    return bool(char_set & SPECIAL_CHARS)

if __name__ == '__main__':
    sample_text_1 = "HelloWorld"
    sample_text_2 = "Hello@World!"
    result_1 = contains_special_characters(sample_text_1)
    result_2 = contains_special_characters(sample_text_2)
    print(result_1)
    print(result_2)