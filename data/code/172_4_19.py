class ConstantWordMapper:
    ONE = "one"
    TWO = "two"
    THREE = "three"

    @staticmethod
    def get_word_mapping():
        return {
            ConstantWordMapper.ONE: "one",
            ConstantWordMapper.TWO: "two",
            ConstantWordMapper.THREE: "three"
        }

if __name__ == '__main__':
    mapper = ConstantWordMapper()
    word_mapping = mapper.get_word_mapping()
    print(word_mapping)