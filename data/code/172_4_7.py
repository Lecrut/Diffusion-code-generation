class ConstantWordMapper:
    WORD_MAP = {
        "ONE": "one",
        "TWO": "two",
        "THREE": "three"
    }

    @staticmethod
    def get_word(key):
        return ConstantWordMapper.WORD_MAP.get(key, None)

if __name__ == '__main__':
    mapper = ConstantWordMapper()
    print(mapper.get_word("ONE"))
    print(mapper.get_word("TWO"))
    print(mapper.get_word("THREE"))
    print(mapper.get_word("FOUR"))