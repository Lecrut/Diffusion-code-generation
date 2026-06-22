class BooleanInverter:
    TRUE_VAL = True
    FALSE_VAL = False

    @staticmethod
    def get_inverted_value(flag: bool) -> bool:
        if flag:
            return BooleanInverter.FALSE_VAL
        return BooleanInverter.TRUE_VAL

if __name__ == '__main__':
    invertor = BooleanInverter()
    original = True
    inverted = invertor.get_inverted_value(original)
    print(inverted)
    original = False
    inverted = invertor.get_inverted_value(original)
    print(inverted)