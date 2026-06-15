def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    text_lower = text.lower()
    for word in target_words:
        if word.lower() in text_lower.split():
            found_matches.append(word)
    return bool(found_matches), found_matches
if __name__ == '__main__':
    input_string = "The quick brown fox jumps over the lazy dog and the fox is quick."
    target_words_list = ["quick", "fox", "lazy", "cat"]
    overall_present, matches = check_multiple_words(input_string, target_words_list)
    print(f"Overall Presence: {overall_present}")
    if matches:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")