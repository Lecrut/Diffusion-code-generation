class SpaceReplacer:
    def __init__(self, text):
        self.text = text

    def replace_spaces(self):
        return self.text.replace(" ", "_")

    def get_original(self):
        return self.text

if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    replacer = SpaceReplacer(sample_text)
    print(replacer.get_original())
    print(replacer.replace_spaces())