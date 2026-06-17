def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_string = "Hello world, this is Python."
    result_list = split_words(sample_string)
    print(result_list)