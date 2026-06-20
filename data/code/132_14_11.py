class XORCalculator:
    @staticmethod
    def xor(a: bool, b: bool) -> bool:
        return (a + b) % 2 == 1

if __name__ == '__main__':
    print(XORCalculator.xor(True, False))
    print(XORCalculator.xor(False, True))
    print(XORCalculator.xor(True, True))
    print(XORCalculator.xor(False, False))