def get_first_letter(text: str) -> str:
    """Returns the first letter of a string if it exists, otherwise returns an empty string."""
    return text[0] if len(text) > 0 else ""

if __name__ == '__main__':
    sample1 = "Hello"
    result1 = get_first_letter(sample1)

    sample2 = ""
    result2 = get_first_letter(sample2)

    print(f'Input: "{sample1}" -> Output: {result1}')
    print(f'Input: "{sample2}" -> Output: {result2}')