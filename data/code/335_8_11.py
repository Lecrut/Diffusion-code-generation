def split_string(text: str, delimiter: str) -> list[str]:
    return text.split(delimiter)
if __name__ == '__main__':
    sample_text = "apple;banana;cherry"
    sample_delimiter = ";"
    result = split_string(sample_text, sample_delimiter)
    print(result)