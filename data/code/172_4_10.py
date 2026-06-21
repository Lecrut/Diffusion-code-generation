class ConstantWordMapper:
    @staticmethod
    def map_constants_to_words():
        return {
            "ONE": "one",
            "TWO": "two",
            "THREE": "three"
        }

if __name__ == '__main__':
    mapper = ConstantWordMapper()
    result = mapper.map_constants_to_words()
    print(result)