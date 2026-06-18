def split_into_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_string = "Hello world Python programming"
    result_list = split_into_words(sample_string)
    print(result_list)