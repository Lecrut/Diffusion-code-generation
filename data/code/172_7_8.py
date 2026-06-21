class WordMapper:
    WORD_MAP = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }

    @staticmethod
    def get_word(code):
        return WordMapper.WORD_MAP.get(code, "unknown")

if __name__ == '__main__':
    sample_codes = [1, 2, 6]
    for code in sample_codes:
        print(f"Code {code}: {WordMapper.get_word(code)}")