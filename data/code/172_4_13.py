class ConstantWordMapper:
    def __init__(self):
        self.mapping = {
            "ONE": "one",
            "TWO": "two",
            "THREE": "three"
        }

    def get_word(self, key):
        return self.mapping.get(key, None)

if __name__ == '__main__':
    mapper = ConstantWordMapper()
    print(mapper.get_word("ONE"))
    print(mapper.get_word("TWO"))
    print(mapper.get_word("THREE"))
    print(mapper.get_word("FOUR"))