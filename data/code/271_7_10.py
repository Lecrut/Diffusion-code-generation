class CharacterTypeCounter:
    UPPERCASE = 'uppercase'
    LOWERCASE = 'lowercase'
    DIGITS = 'digits'
    PUNCTUATION = 'punctuation'

    @staticmethod
    def count_character_types(text):
        counts = {
            CharacterTypeCounter.UPPERCASE: 0,
            CharacterTypeCounter.LOWERCASE: 0,
            CharacterTypeCounter.DIGITS: 0,
            CharacterTypeCounter.PUNCTUATION: 0
        }
        for char in text:
            if char.isupper():
                counts[CharacterTypeCounter.UPPERCASE] += 1
            elif char.islower():
                counts[CharacterTypeCounter.LOWERCASE] += 1
            elif char.isdigit():
                counts[CharacterTypeCounter.DIGITS] += 1
            else:
                counts[CharacterTypeCounter.PUNCTUATION] += 1
        return counts

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = CharacterTypeCounter.count_character_types(sample_text)
    print(result)