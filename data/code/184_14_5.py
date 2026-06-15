def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    lower_text = text.lower()
    for target in target_words:
        if target.lower() in lower_text:
            found_matches.append(target)
    return bool(found_matches), found_matches
if __name__ == '__main__':
    input_string = "The quick brown fox jumps over the lazy dog and the fox is clever."
    words_to_find = ["fox", "dog", "cat", "bird"]
    overall_present, matches = check_multiple_words(input_string, words_to_find)
    print(f"Overall Presence: {overall_present}")
    if overall_present:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")