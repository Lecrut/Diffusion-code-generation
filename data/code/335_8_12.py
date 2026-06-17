def split_string(text: str, delimiter: str) -> list[str]:
    return text.split(delimiter)
if __name__ == '__main__':
    sample_text = "apple;banana;cherry"
    sample_delimiter = ";"
    result_parts = split_string(sample_text, sample_delimiter)
    print(f"Original: {sample_text}")
    print(f"Delimiter: '{sample_delimiter}'")
    print("Split parts:")
    for part in result_parts:
        print(part)