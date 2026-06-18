def split_string_into_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world Python programming"
    result_list = split_string_into_words(sample_text)
    print(result_list)