class AsteriskPattern:
    CHAR_CONSTANT = '*'
    
    @staticmethod
    def _build_row(length: int) -> str:
        return AsteriskPattern.CHAR_CONSTANT * length

    @staticmethod
    def generate(size: int) -> str:
        return '\n'.join(AsteriskPattern._build_row(size) for _ in range(size))

if __name__ == '__main__':
    result = AsteriskPattern.generate(10)
    print(result)