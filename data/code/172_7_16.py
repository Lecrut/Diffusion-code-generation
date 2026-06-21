class WordCodeMapper:
    CODE_TO_WORD = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }

    @classmethod
    def get_word(cls, code):
        return cls.CODE_TO_WORD.get(code, "unknown")

if __name__ == '__main__':
    mapper = WordCodeMapper()
    print(f"Word for code 3: {mapper.get_word(3)}")
    print(f"Word for code 6: {mapper.get_word(6)}")