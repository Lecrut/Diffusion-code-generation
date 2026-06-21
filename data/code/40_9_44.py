def get_first_letters(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list")
    for s in strings:
        if not isinstance(s, str) or not s:
            raise ValueError("All elements in the list must be non-empty strings")
    return [s[0] for s in strings]

if __name__ == '__main__':
    sample_values = ["strawberry", "tangerine", "ugli fruit", "vanilla"]
    result = get_first_letters(sample_values)
    print(result)