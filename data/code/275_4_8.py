class UniqueCharacters:

    @staticmethod
    def are_unique(characters):
        seen = set()
        for char in characters:
            if char in seen:
                return False
            seen.add(char)
        return True
if __name__ == '__main__':
    sample_chars = 'abcdefg'
    result = UniqueCharacters.are_unique(sample_chars)
    print(result)
    sample_chars_with_duplicates = 'abcdeafg'
    result = UniqueCharacters.are_unique(sample_chars_with_duplicates)
    print(result)