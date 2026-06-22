class BitwiseOrLogic:
    _TRUE_BIT = 1
    _FALSE_BIT = 0

    @staticmethod
    def _to_bit(val):
        return 1 if val else 0

    @staticmethod
    def check_or_condition(a: bool, b: bool) -> bool:
        result_bit = BitwiseOrLogic._to_bit(a) | BitwiseOrLogic._to_bit(b)
        return result_bit == BitwiseOrLogic._TRUE_BIT

if __name__ == '__main__':
    result = BitwiseOrLogic.check_or_condition(True, False)
    print(result)