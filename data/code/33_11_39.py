class SpaceRemover:
    def __init__(self):
        self.translation_table = str.maketrans('', '', ' ')

    def remove_spaces(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.translate(self.translation_table)

if __name__ == '__main__':
    remover = SpaceRemover()
    sample_text1 = "This is a sample text with spaces."
    sample_text2 = 'Another example without any spaces.'
    sample_text3 = "Yet another variant with multiple spaces."

    print(remover.remove_spaces(sample_text1))
    print(remover.remove_spaces(sample_text2))
    print(remover.remove_spaces(sample_text3))