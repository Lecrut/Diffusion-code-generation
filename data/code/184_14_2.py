import re
def check_multiple_words(text: str, target_words: list[str]) -> tuple[bool, list[str]]:
    found_matches = []
    text_lower = text.lower()
    for word in target_words:
        if word.lower() in text_lower:
            found_matches.append(word)
    return bool(found_matches), found_matches
if __name__ == '__main__':
    input_string = "The quick brown fox jumps over the lazy dog. Fox is clever."
    target_words_to_find = ["fox", "dog", "cat"]
    overall_present, matches = check_multiple_words(input_string, target_words_to_find)
    print(f"Overall Presence: {overall_present}")
    if matches:
        print("Found Matches:")
        for match in matches:
            print(f"- {match}")
    else:
        print("No target words found.")