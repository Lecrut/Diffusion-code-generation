def split_string(s: str, delimiter: str) -> list[str]:
    return s.split(delimiter)
if __name__ == '__main__':
    sample_str = "apple;banana;cherry"
    sample_delim = ";"
    result = split_string(sample_str, sample_delim)
    print(result)