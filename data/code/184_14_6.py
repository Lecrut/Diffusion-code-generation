def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    text_lower = text.lower()
    for target in target_words:
        if target.lower() in text_lower:
            start_index = -1
            while True:
                start_index = text_lower.find(target.lower(), start_index + 1)
                if start_index == -1:
                    break
                found_matches.append(text[start_index:start_index + len(target)])
    return bool(found_matches), found_matches
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_words = ["fox", "dog", "cat"]
    overall_presence, matches = check_multiple_words(sample_text, target_words)
    print(f"Overall Presence: {overall_presence}")
    if matches:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")
    else:
        print("No specific words found.")