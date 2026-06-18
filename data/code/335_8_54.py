def split_string_by_delimiter(text: str, delimiter: str) -> list[str]:
    return [part for part in text.split(delimiter)]
if __name__ == '__main__':
    sample_text = "apple;banana;cherry"
    sample_delimiter = ";"
    result = split_string_by_delimiter(sample_text, sample_delimiter)
    print(result)