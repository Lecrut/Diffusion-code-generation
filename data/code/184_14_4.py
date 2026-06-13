def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    lower_text = text.lower()
    for word in target_words:
        if word.lower() in lower_text.lower():
            found_matches.append(word)
    return bool(found_matches), found_matches
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_words = ["fox", "dog", "cat", "bird"]
    overall_present, matches = check_multiple_words(sample_text, target_words)
    print(f"Overall Presence: {overall_present}")
    if matches:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")