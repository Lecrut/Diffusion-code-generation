class SpaceReplacer:
    _SPACE_CHAR = " "
    _REPLACEMENT_CHAR = "_"

    def __init__(self, text: str):
        self._original_text = text

    def get_result(self) -> str:
        text = self._original_text
        if text == "":
            return ""
        if self._SPACE_CHAR not in text:
            return text
        return text.replace(self._SPACE_CHAR, self._REPLACEMENT_CHAR)

if __name__ == '__main__':
    sample_input = "Python Code Snippet"
    replacer = SpaceReplacer(sample_input)
    output = replacer.get_result()
    print(output)