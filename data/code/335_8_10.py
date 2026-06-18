def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    sample_text = "apple;banana;cherry"
    result = split_string(sample_text, ";")
    print(result)