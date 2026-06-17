def split_string_to_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world Python programming"
    result_list = split_string_to_words(sample_text)
    print(f"Input: {sample_text}")
    print(f"Output list: {result_list}")