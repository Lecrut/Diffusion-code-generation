def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    text_lower = text.lower()
    for target in target_words:
        if target.lower() in text_lower:
            found_matches.append(target)
    return bool(found_matches), found_matches
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_words = ["fox", "dog", "cat", "bird"]
    overall_present, matches = check_multiple_words(sample_text, target_words)
    print(f"Overall Presence: {overall_present}")
    if overall_present:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")