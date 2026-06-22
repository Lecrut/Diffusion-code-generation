def find_words_with_substring(text: str, substring: str) -> list:
    if not isinstance(text, str) or not isinstance(substring, str):
        raise ValueError("Both text and substring must be strings.")
    
    words = text.split()
    filtered_words = [word for word in words if substring in word]
    return filtered_words

if __name__ == '__main__':
    sample_text = "Hello world, this is a test string with the substring 'test'."
    sample_substring = 'test'
    result = find_words_with_substring(sample_text, sample_substring)
    print(result)