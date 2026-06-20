class XOR:
    @staticmethod
    def xor(a: bool, b: bool) -> bool:
        return (a + b) % 2 == 1

if __name__ == '__main__':
    print(XOR.xor(True, False))
    print(XOR.xor(False, True))
    print(XOR.xor(True, True))
    print(XOR.xor(False, False))