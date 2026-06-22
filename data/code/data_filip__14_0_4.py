def are_characters_unique(text: str) -> bool:
    character_set = set()
    for current_character in text:
        if current_character in character_set:
            return False
        character_set.add(current_character)
    return True

if __name__ == '__main__':
    sample_string = "python"
    is_unique = are_characters_unique(sample_string)
    print(is_unique)