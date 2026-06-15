def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    lower_text = text.lower()
    for word in target_words:
        if word.lower() in lower_text.lower():
            found_matches.append(word)
    overall_presence = bool(found_matches)
    return overall_presence, found_matches
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog and the fox is clever."
    target_words = ["fox", "dog", "cat", "bird"]
    overall_result, matches = check_multiple_words(sample_text, target_words)
    print(f"Overall Presence: {overall_result}")
    if matches:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")