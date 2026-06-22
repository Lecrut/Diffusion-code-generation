class TextTransformer:
    SPACE_CHARACTER = " "
    UNDERSCORE_CHARACTER = "_"

    @staticmethod
    def replace_spaces(text):
        return text.replace(TextTransformer.SPACE_CHARACTER, TextTransformer.UNDERSCORE_CHARACTER)

if __name__ == '__main__':
    original = "replace these spaces"
    print(TextTransformer.replace_spaces(original))