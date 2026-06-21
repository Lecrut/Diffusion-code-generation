class BinaryConverter:
    ZERO = "0"
    ONE = "1"

    @staticmethod
    def to_binary(n):
        if n == 0:
            return BinaryConverter.ZERO
        result = []
        while n > 0:
            if n & 1:
                result.append(BinaryConverter.ONE)
            else:
                result.append(BinaryConverter.ZERO)
            n >>= 1
        return "".join(reversed(result))

if __name__ == "__main__":
    print(BinaryConverter.to_binary(0))
    print(BinaryConverter.to_binary(1))
    print(BinaryConverter.to_binary(5))
    print(BinaryConverter.to_binary(10))
    print(BinaryConverter.to_binary(255))
    print(BinaryConverter.to_binary(1024))