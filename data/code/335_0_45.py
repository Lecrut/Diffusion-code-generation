def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world, this is Python programming."
    result_list = split_words(sample_text)
    assert isinstance(result_list, list), "Result must be a list"
    expected_count = 6
    actual_count = len(result_list)
    if actual_count != expected_count:
        raise AssertionError(f"Expected {expected_count} words but got {actual_count}")