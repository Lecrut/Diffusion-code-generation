class SpaceReplacer:
    SOURCE_SPACE = ' '
    TARGET_UNDERSCORE = '_'

    @staticmethod
    def convert(text):
        return text.replace(SpaceReplacer.SOURCE_SPACE, SpaceReplacer.TARGET_UNDERSCORE)

if __name__ == '__main__':
    sample = "the quick brown fox"
    result = SpaceReplacer.convert(sample)
    print(result)