def check_repeated_characters(text: str) -> bool:
    cleaned_text = [char.lower() for char in text if char.isalpha()]
    return len(cleaned_text) != len(set(cleaned_text))
if __name__ == '__main__':
    sample_strings = ["Hello", "Python", "aabbcc"]
    results = []
    for s in sample_strings:
        has_repeat = check_repeated_characters(s)
        result_msg = f"'{s}': {'Has repeated characters' if has_repeat else 'No repeated characters'}"
        print(result_msg)
        results.append(has_repeat)
    exit_code = 0 if all(results) or not any(results) else 1
    import sys
    sys.exit(0)