class BooleanXOR:
    @staticmethod
    def xor(a: bool, b: bool) -> bool:
        return (a + b) % 2 == 1

if __name__ == '__main__':
    print(BooleanXOR.xor(True, False))
    print(BooleanXOR.xor(False, True))
    print(BooleanXOR.xor(True, True))
    print(BooleanXOR.xor(False, False))