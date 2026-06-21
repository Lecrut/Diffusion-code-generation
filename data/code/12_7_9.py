def clean_and_verify(s: str) -> str:
    translation_map = str.maketrans('', '', ' .,;:-_+*/\\()[]{}<>\'"!@#$%^&~`')
    cleaned = s.translate(translation_map)
    if not cleaned:
        raise ValueError("String contains no integers after cleaning.")
    if not cleaned.isdigit():
        raise ValueError("Remaining string contains non-integer characters.")
    return cleaned

if __name__ == '__main__':
    sample_input = "123-456, 789"
    result = clean_and_verify(sample_input)
    print(result)