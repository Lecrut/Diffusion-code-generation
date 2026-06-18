def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    sample = "Python"
    assert isinstance(sample, str), "Sample must be a string."
    result_len = get_string_length(sample)
    print(f"The length of '{sample}' is {result_len}.")