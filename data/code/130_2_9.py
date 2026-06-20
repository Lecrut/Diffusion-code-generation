class ZeroVerifier:
    ZERO_VALUES = (0, 0.0)

    @staticmethod
    def is_zero(value):
        return value in ZeroVerifier.ZERO_VALUES

if __name__ == '__main__':
    print(ZeroVerifier.is_zero(0))
    print(ZeroVerifier.is_zero(0.0))
    print(ZeroVerifier.is_zero(-0))
    print(ZeroVerifier.is_zero(-0.0))
    print(ZeroVerifier.is_zero(1))
    print(ZeroVerifier.is_zero(1.0))