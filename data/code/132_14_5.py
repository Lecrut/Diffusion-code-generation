class XORLogic:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def bool_to_int(b: bool) -> int:
        return XORLogic.TRUE if b else XORLogic.FALSE

    @staticmethod
    def xor(a: bool, b: bool) -> bool:
        return bool(XORLogic.bool_to_int(a) ^ XORLogic.bool_to_int(b))

if __name__ == '__main__':
    print(XORLogic.xor(True, False))
    print(XORLogic.xor(False, True))
    print(XORLogic.xor(True, True))
    print(XORLogic.xor(False, False))