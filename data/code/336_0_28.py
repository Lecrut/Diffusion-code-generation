def check_repeated_characters(text: str) -> bool:
    cleaned_text = [char.lower() for char in text if char.isalpha()]
    return len(cleaned_text) != len(set(cleaned_text))
if __name__ == '__main__':
    sample_strings = ["Hello", "Python", "AaBbCc"]
    has_repeated = False
    print("Checking for repeated characters:")
    for s in sample_strings:
        result = check_repeated_characters(s)
        if result:
            has_repeated = True
            status = "Has repeated characters"
        else:
            status = "No repeated characters"
        print(f"'{s}': {status}")
    final_output = "Repeated character found in sample strings." if has_repeated else "No repeated characters found in any of the sample strings."
    combined_text = "".join(sample_strings)
    is_combined_ok = not check_repeated_characters(combined_text)
    print(f"\nCombined text '{combined_text}': {status if 'Has' in status else 'No repeated characters'}")
    exit(0)