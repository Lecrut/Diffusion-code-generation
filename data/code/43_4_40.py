class Square:
    MIN_SIDE_LENGTH = 0.0

    @staticmethod
    def calculate_area(side_length: float) -> float:
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")
        return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4.5
    area = Square.calculate_area(sample_side_length)
    print(area)