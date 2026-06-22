class SpaceReplacer:
    _FIND_CHAR = ' '
    _REPLACE_CHAR = '_'

    @staticmethod
    def replace(text: str) -> str:
        return text.replace(SpaceReplacer._FIND_CHAR, SpaceReplacer._REPLACE_CHAR)

if __name__ == '__main__':
    input_string = "Replace spaces now"
    output = SpaceReplacer.replace(input_string)
    print(output)