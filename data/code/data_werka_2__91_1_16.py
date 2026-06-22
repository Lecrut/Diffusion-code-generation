class BooleanInverter:
    @classmethod
    def invert(cls, flag: bool) -> bool:
        return not flag

if __name__ == '__main__':
    result_true = BooleanInverter.invert(True)
    result_false = BooleanInverter.invert(False)
    print(result_true)
    print(result_false)