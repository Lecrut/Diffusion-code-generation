class SquareCalculator:
    SIDE_LENGTH = 7

    @staticmethod
    def get_area(length: int) -> int:
        return length ** 2

    @classmethod
    def run(cls) -> int:
        return cls.get_area(cls.SIDE_LENGTH)

if __name__ == '__main__':
    result = SquareCalculator.run()
    print(result)