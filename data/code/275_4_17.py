class CharacterUniquenessChecker:
    @staticmethod
    def are_characters_unique(characters):
        return len(characters) == len(set(characters))

if __name__ == '__main__':
    sample_characters = "abcdefg"
    result = CharacterUniquenessChecker.are_characters_unique(sample_characters)
    print(result)