def split_string(s: str) -> list[str]:
    return s.split()
if __name__ == '__main__':
    sample_text = "apple banana cherry date"
    result = split_string(sample_text)
    print(result)