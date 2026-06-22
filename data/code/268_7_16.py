class SentenceParser:
    PUNCTUATION = ",.!?;:"

    @staticmethod
    def remove_punctuation(word):
        while word and word[-1] in SentenceParser.PUNCTUATION:
            word = word[:-1]
        return word

    @classmethod
    def extract_first_word(cls, text):
        parts = text.split()
        if parts:
            first_part = parts[0].strip(cls.PUNCTUATION)
            return cls.remove_punctuation(first_part)
        else:
            return ""

if __name__ == '__main__':
    parser = SentenceParser()
    sample_string1 = "This is a sample sentence."
    result1 = parser.extract_first_word(sample_string1)
    print(result1)

    sample_string2 = "  leading spaces and multiple words, "
    result2 = parser.extract_first_word(sample_string2)
    print(result2)

    sample_string3 = "singleword!"
    result3 = parser.extract_first_word(sample_string3)
    print(result3)

    sample_string4 = ""
    result4 = parser.extract_first_word(sample_string4)
    print(result4)