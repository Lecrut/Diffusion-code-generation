def calculate_string_length(text: str) -> int:
    """Returns the total number of characters in the input string, 
    including spaces and punctuation."""
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external inputs are required.
    sample_1 = "Hello World!"
    sample_2 = "Python is powerful."

    length_1 = calculate_string_length(sample_1)
    print(f"Length of '{sample_1}': {length_1}")

    length_2 = calculate_string_length(sample_2)
    print(f"Length of '{sample_2}': {length_2}")