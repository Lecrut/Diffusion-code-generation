CODE_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

class CodeWordMapper:
    def __init__(self, mapping=CODE_MAP):
        self._mapping = mapping

    def get_word(self, code):
        return self._mapping.get(code, "unknown")

if __name__ == '__main__':
    mapper = CodeWordMapper()
    print("Code 1 maps to:", mapper.get_word(1))
    print("Code 6 maps to:", mapper.get_word(6))