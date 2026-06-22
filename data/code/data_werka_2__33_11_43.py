class SpaceEliminator:
    def __init__(self):
        self.space_translation = str.maketrans('', '', ' ')
    
    def eliminate_spaces(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.translate(self.space_translation)

if __name__ == '__main__':
    eliminator = SpaceEliminator()
    sample_text1 = "This is the first sample with spaces."
    sample_text2 = "Another example here too."
    sample_text3 = "One more instance of space elimination."

    print(eliminator.eliminate_spaces(sample_text1))
    print(eliminator.eliminate_spaces(sample_text2))
    print(eliminator.eliminate_spaces(sample_text3))