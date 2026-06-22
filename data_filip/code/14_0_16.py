def is_string_unique(s: str) -> bool:
    char_tracker = set()
    for current_character in s:
        if current_character in char_tracker:
            return False
        char_tracker.add(current_character)
    return True

if __name__ == '__main__':
    sample_input = "algorithm"
    output = is_string_unique(sample_input)
    print(output)