class WordCombiner:
    def __init__(self):
        pass
    def combine_strings(self, str1, str2):
        return f"{str1} {str2}"
if __name__ == '__main__':
    word_combiner = WordCombiner()
    result = word_combiner.combine_strings("Hello", "World")
    print(result)