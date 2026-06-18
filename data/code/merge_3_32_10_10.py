def calculate_string_length(text: str) -> int:
    """Calculate the total character length of a string, including spaces and punctuation."""
    return len(text)

if __name__ == '__main__':
    # Sample inputs without user interaction or external dependencies
    sample_text_1 = "Hello World! This is a test case."
    sample_text_2 = ""

    result_1 = calculate_string_length(sample_text_1)
    print(f"Length of '{sample_text_1}': {result_1}")

    result_2 = calculate_string_length(sample_text_2)
    print(f"Length of 'empty string': {result_2}")